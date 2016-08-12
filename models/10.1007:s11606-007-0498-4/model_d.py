"""
model_d.py
by Ted Morin

contains a function to predict ACS patient 1 Year Mortality risks after 30 Days using nomogram from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
  
(Figures 2 and 3)

function expects parameters of:
    Male Sex        Age     Creatinine Clearance     Weight     Hemoglobin      
        bool       float            float            float        float
                    years           mL/min            kg           g/dL
    
function parameters continued...
    Platelets           Nadir Platelets     Atrial Fibrillation 
       float               float                bool
      10^3/mm^3           10^3/mm^3         
    
function parameters continued...
    Statins at 30 Days              Coronary Artery Bypass Grafting within 30 days
        bool                                        bool
"""     

def model(ismale, age, crea_clear, weight, hemo, plate, nadir_plate, af, stat30, cabg30):
    
    # age
    if age <= 35: age = 0
    elif age <= 45 : age = 4
    elif age <= 55 : age = 7
    elif age <= 65 : age = 11
    elif age <= 75 : age = 15
    elif age <= 85 : age = 18
    else : age = 20
    
    # crea_clear
    if crea_clear < 0 + 5: crea_clear = 56
    elif crea_clear <  10 + 5 : crea_clear = 51
    elif crea_clear <  20 + 5 : crea_clear = 46
    elif crea_clear <  30 + 5 : crea_clear = 41
    elif crea_clear <  40 + 5 : crea_clear = 35
    elif crea_clear <  50 + 5 : crea_clear = 30
    elif crea_clear <  60 + 5 : crea_clear = 25
    elif crea_clear <  70 + 5 : crea_clear = 20
    elif crea_clear <  80 + 5 : crea_clear = 15
    elif crea_clear <  90 + 5 : crea_clear = 10
    elif crea_clear < 100 + 5 : crea_clear = 5
    else : crea_clear = 0
    
    # weight
    if weight < 20 + 10: weight = 43
    elif weight <  40 + 10 : weight = 22
    elif weight <  60 + 10 : weight = 0
    elif weight <  80 + 10 : weight = 5
    elif weight < 100 + 10 : weight = 11
    elif weight < 120 + 10 : weight = 16
    elif weight < 140 + 10 : weight = 22
    else : weight = 27
    
    # hemo
    if hemo < 5 + 0.5: hemo = 74
    elif hemo <  6 + 0.5: hemo = 67
    elif hemo <  7 + 0.5: hemo = 59
    elif hemo <  8 + 0.5: hemo = 52
    elif hemo <  9 + 0.5: hemo = 45
    elif hemo < 10 + 0.5: hemo = 37
    elif hemo < 11 + 0.5: hemo = 30
    elif hemo < 12 + 0.5: hemo = 22
    elif hemo < 13 + 0.5: hemo = 15
    elif hemo < 14 + 0.5: hemo = 7
    else : hemo = 0
    
    # plate
    if plate < 200 + 50: plate = 0
    elif plate < 300 + 50: plate = 13
    elif plate < 400 + 50: plate = 25
    elif plate < 500 + 50: plate = 37
    elif plate < 600 + 50: plate = 50
    elif plate < 700 + 50: plate = 62
    elif plate < 800 + 50: plate = 75
    elif plate < 900 + 50: plate = 87
    else : plate = 100
    
    # nadir_plate
    if nadir_plate < 0 + 10 : nadir_plate = 48
    elif nadir_plate <  20 + 10 : nadir_plate = 43
    elif nadir_plate <  40 + 10 : nadir_plate = 38
    elif nadir_plate <  60 + 10 : nadir_plate = 33
    elif nadir_plate <  80 + 10 : nadir_plate = 29
    elif nadir_plate < 100 + 10 : nadir_plate = 24
    elif nadir_plate < 120 + 10 : nadir_plate = 19
    elif nadir_plate < 140 + 10 : nadir_plate = 14
    elif nadir_plate < 160 + 10 : nadir_plate = 10
    elif nadir_plate < 180 + 10 : nadir_plate = 5
    else : nadir_plate = 0
    
    # af
    af = af * 23
    # stat30
    if not stat30:
        stat30 = 17
    # cabg30
    if not cabg30:
        cabg30 = 20
    # ismale
    ismale = ismale * 20
    
    score = ismale + age + crea_clear + weight + hemo + plate + nadir_plate + af + stat30 + cabg30
    
    if   score < float(64 + 107)/2: risk = .01
    elif score < float(107 + 127)/2: risk = 0.05
    elif score < float(127 + 138)/2: risk = 0.1
    elif score < float(138 + 147)/2: risk = 0.15
    elif score < float(147 + 159)/2: risk = 0.2
    elif score < float(159 + 169)/2: risk = 0.3
    elif score < float(169 + 177)/2: risk = 0.4
    elif score < float(177 + 184)/2: risk = 0.5
    elif score < float(184 + 191)/2: risk = 0.6
    elif score < float(191 + 199)/2: risk = 0.7
    elif score < float(199 + 209)/2: risk = 0.8
    else : risk = 0.9
    
    return risk
