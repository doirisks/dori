"""
model_a.py
by Ted Morin

contains a function to predict 2.5-year Intracranial Bleeding risks using PANWARDS Nomogram Point system from
10.1161/STROKEAHA.113.004506
2014 Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban

Note 1: function returns an estimate based on the shown values of the PANWARDS Nomogram - no formula is reproduced
  
Note 2: "White/Other" Ethnicity is assumed if non is given


function expects parameters of
    Age     Diastolic Blood Pressure    Platelets   Albumin     History of Coronary Heart Failure
   float            float               float       float                   bool
   years            mmHg                10^9/L      g/dL

parameters continued...
History of Stroke or TIA     Asian Ethnicity    Black Ethnicity     Warfarin        Rivaroxaban
        bool                        bool            bool              bool              bool
"""        

def model(age, dbp, plate, albu, hx_chf, hx_str_or_tia, asian, black, warfa, rivar):
    points = 0 
    
    # platelets
    if plate < 125 : 
        points += 11
    elif plate < 150 :
        points += 8
    elif plate < 175 :
        points += 5
    elif plate < 200 :
        points += 3
    else :
        points += 0
    
    # albumin
    if albu < 3.0 :
        points += 18
    elif albu < 3.5 :
        points += 14
    elif albu < 4.0 :
        points += 9
    elif albu < 4.5 :
        points += 5
    else :
        points += 0
        
    # History of Coronary Heart Failure
    if not hx_chf :
        points += 6
        
    # warfarin vs. rivaroxaban
    if warfa :
        points += 7
        
    # age
    if age < 55 : 
        points += 0
    elif age < 65 :
        points += 4
    elif age < 75 :
        points += 8
    elif age < 85 :
        points += 13
    else :
        points += 17
        
    # race
    if black :
        points += 18
    elif asian :
        points += 9
    else :
        points += 0
    
    # Diastolic Blood Pressure
    
    if dbp < 50 :
        points += 0
    elif dbp < 70 :
        points += 4
    elif dbp < 90 :
        points += 9
    elif dbp < 110 :
        points += 13
    else :
        points += 17
      
    # history of stroke or transient ischemic attack  
    if hx_str_or_tia:
        points += 5
        
    # PANWARDS scores and risks - calculation
    scores = [   10,    15,    20,    25,    30,    35,    40,    45,    50,    55,   60,    65,    70,   75]
    risks  = [0.002, 0.003, 0.004, 0.006, 0.008, 0.012, 0.017, 0.025, 0.035, 0.049, 0.07, 0.098, 0.137, 0.19]
    
    if points < scores[0]:
        m = (risks[0] - 0) / (scores[0] - 0)
        return m * points
    for i in range(1, len(scores)):
        if points < scores[i]:
            m = (risks[i] - risks[i-1]) / (scores[i] - scores[i-1])
            return risks[i-1] + m * (points - scores[i-1])
    i = len(scores) - 1
    m = (risks[i] - risks[i-1]) / (scores[i] - scores[i-1])
    return risks[i] + m * (points - scores[i])
