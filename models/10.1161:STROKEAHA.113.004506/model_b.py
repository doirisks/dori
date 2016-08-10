"""
model_b.py
by Ted Morin

contains a function to predict 2.5?-year Hemorrhagic Stroke risks using Cox Model from
10.1161/STROKEAHA.113.004506
2014 Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban
  
Note 1: "White/Other" Ethnicity is assumed if non is given


function expects parameters of
    Age     Diastolic Blood Pressure    Platelets   Albumin     History of Coronary Heart Failure
   float            float               float       float                   bool
   years            mmHg                10^9/L      g/dL

parameters continued...
 Asian Ethnicity    Black Ethnicity     Warfarin        Rivaroxaban
        bool            bool              bool             bool
"""        

def model(age, dbp, plate, albu, hx_chf, asian, black, warfa, rivar):
    # imports
    import math
    
    # betas, s0, xbar_sum
    betas = [
        0.817515256,        # "Age, for 10 year increase above 75"
        -0.572588294,       # "History of CHF"
        0.706310911,        # "race3 Asian"
        0.998770217,        # "race3 Black"
        0.434521459,        # "Albumin, HR for 0.5 unit decrease"
        0.714195665,        # "DBP (10mmHg increase above 85)"
        0.099045904,        # "Platelets (linear spline to 210)"
        -0.503614198        # "Randomized Rivaroxaban"
    ]
    s0 = 0.991642329
    xbar_sum = 2.07996542626
    
    # derivation/scaling of variables and linear splines

    if age > 75:
        age = (float(age) - 75.) /10
    else :
        age = 0

    if dbp > 85 :
        dbp = (float(dbp) - 85) /10
    else :
        dbp = 0
    
    albu = -albu / 0.5
    
    if plate < 210:
        plate = 210.0 - float(plate)
    else :
        plate = 0
    plate = plate/10
        
    # independent variable list
    xvals = [
        age,            # "Age, for 10 year increase above 75"
        hx_chf,         # "History of CHF"
        asian,          # "race3 Asian"
        black,          # "race3 Black"
        albu,           # "Albumin, HR for 0.5 unit decrease"
        dbp,            # "DBP (10mmHg increase above 85)"
        plate,          # "Platelets (linear spline to 210)"
        rivar           # "Randomized Rivaroxaban"
    ]
    
    # dot product
    xsum = 0 
    for i, beta in enumerate(betas):
        xsum += beta * xvals[i]
    
    # subtract the xbar_sum
    xsum -= xbar_sum
    
    risk = 1 - math.pow(s0, math.exp(xsum))
    
    return risk
