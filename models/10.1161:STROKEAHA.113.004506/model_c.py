"""
model_c.py
by Ted Morin

contains a function to predict 2.5?-year Intracranial Bleeding risks using Cox Model from
10.1161/STROKEAHA.113.004506
2014 Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban
  
Note 1: "White/Other" Ethnicity is assumed if none is given

function expects parameters of
    Age     Diastolic Blood Pressure    Platelets   Albumin     History of Coronary Heart Failure
   float            float               float       float                   bool
   years            mmHg                10^9/L      g/dL

parameters continued...
History of Stroke or TIA     Asian Ethnicity    Black Ethnicity     Warfarin        Rivaroxaban
        bool                        bool            bool              bool              bool
"""        

def model(age, dbp, plate, albu, hx_chf, hx_str_or_tia, asian, black, warfa, rivar):
    # imports
    import math
    
    # betas, s0, xbar_sum
    betas = [
        0.3037294316,       # "Age, for 10 year increase above 75"
        -0.4362316697,      # "History of CHF"
        0.7031173301,       # "race3 Asian"
        1.178916448,        # "race3 Black"
        0.3305890214,       # "Albumin, HR for 0.5 unit decrease"
        0.1572762413,       # "DBP (10mmHg increase above 85)"
        0.0754477288,       # "Platelets (linear spline to 210)"
        -0.5130761361,      # "Randomized Rivaroxaban"
        0.347371734         # "History of stroke or TIA"
    ]
    s0 = 0.9762903037
    xbar_sum = -2.03041903621
    
    # derivation/scaling of variables and linear splines

    age = (float(age) - 75.) /10

    dbp = (float(dbp) - 85) /10
    
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
        rivar,          # "Randomized Rivaroxaban"
        hx_str_or_tia   # "History of stroke or TIA"
    ]
    
    # dot product
    xsum = 0 
    for i, beta in enumerate(betas):
        xsum += beta * xvals[i]
    
    # subtract the xbar_sum
    xsum -= xbar_sum
    
    risk = 1 - math.pow(s0, math.exp(xsum))
    
    return risk
