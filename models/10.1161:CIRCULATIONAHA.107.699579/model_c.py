"""
model_c.py
by Ted Morin

contains a function to predict 10-year Stroke risks using model from
10.1161/CIRCULATIONAHA.107.699579
General Cardiovascular Risk Profile for Use in Primary Care
Framingham Heart Study

function expects parameters of
"ismale" "antihypertensive medication use" "age" "total colesterol" "HDL cholesterol" "SBD" "Smoking" "Diabetes"
                                           years      mg/dL               mg/dL       mm Hg
  bool                  bool             int/float   int/float          int/float   int/float  bool      bool
"""        
        
def model(ismale,antihyp,age,totchol,hdlchol,sbp, smoke,diabet):
    
    # imports
    import numpy as np
    
    # beta values
    female_betas = np.array([
        2.32888,    #"Log of age"
        1.20904,    #"Log of total cholesterol"
        -0.70833,   #"Log of HDL cholesterol"
        2.76157,    #"Log of SBP if not treated"
        2.82263,    #"Log of SBP if treated"
        0.52873,    #"Smoking"
        0.69154     #"Diabetes"
    ])
    female_s0 = 0.95012
    female_xbar = 26.1931

    male_betas = np.array([
        3.06117,    #"Log of age"
        1.12370,    #"Log of total cholesterol"
        -0.93263,   #"Log of HDL cholesterol"
        1.93303,    #"Log of SBD if not treated"
        1.99881,    #"Log of SBD if treated"
        0.65451,    #"Smoking"
        0.57367     #"Diabetes"
    ])
    male_s0 = 0.88936
    male_xbar = 23.9802

    #determine which beta values should be used
    betas = None
     
    # accounts for gender
    if ismale :
        betas = male_betas
        s0 = male_s0
        xbar = male_xbar
    else :
        betas = female_betas
        s0 = female_s0
        xbar = female_xbar
     
    # transforms input values logarithmically
    age = np.log(age)
    totchol = np.log(totchol)
    hdlchol = np.log(hdlchol)
    sbp = np.log(sbp)
    
    # accounts for antihypertensive medication
    if antihyp:
        sbp_antihyp = sbp
        sbp_noantihyp = 0.
    else :
        sbp_antihyp = 0.
        sbp_noantihyp = sbp
    
    # builds a numpy array of the values
    values = np.array([age,totchol,hdlchol,sbp_noantihyp,sbp_antihyp,smoke,diabet])
    
    # dots the betas and the values
    value = np.dot(betas,values)
    
    # returns the cox-calculated value
    cvd = 1 - np.power(s0,np.exp(value - xbar))
    
    male_calib_factor   = 0.1590
    female_calib_factor = 0.2385
    
    if ismale:
        return cvd * male_calib_factor
    else :
        return cvd * female_calib_factor
