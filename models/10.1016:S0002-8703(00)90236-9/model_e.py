"""
model_e.py
by Ted Morin

contains a function to predict 2-year subsequent Coronary Heart Disease risks using beta coefficients from 
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study

Uses Weibull model set to 2 years

function expects parameters of
 "sex"   "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "diabetic" "smoker"
  m=T     years        mg/dL            mg/dL            mm Hg      
 bool    int/float    int/float       int/float        int/float      bool       bool  
"""        

def model(ismale, age, totchol, hdlchol, sysBP, diabet, smoker):
    import numpy as np
    
    # betas, s0's, xbars
    male_betas = [
        4.995,              #Intercept
        -0.0145,            #Age
        -0.6738,            #ln(totchol/hdlchol)
        -0.3042            #Diabetes
    ]
    male_s = 0.9994
    
    female_betas = [
        13.537,             #Intercept
        -0.0225,            #Age
        -0.834,             #ln(totchol/hdlchol)
        -1.3713,            #ln(sysBP)
        -0.7829,            #Diabetes
        -0.3669            #Smoker
    ]
    female_s = 1.0313
    
    #prepare derived values
    log_chol_ratio = np.log(float(totchol)/hdlchol)
    
    # a value for the intercept
    intercept = 1
    
    betas = None
    s0 = None
    if ismale :
        values = np.array([intercept,age, log_chol_ratio,diabet])
        betas = np.array(male_betas) 
        s = male_s
    else :
        log_sysBP = np.log(sysBP)
        values = np.array([intercept,age,log_chol_ratio,log_sysBP,diabet, smoker])
        betas = np.array(female_betas)
        s = female_s
    # dot product
    value = np.dot(values, betas)
    
    # calculate using weibull regression model
    t = 2 # valid for 1 <= t <= 4, where t represent the number of years
    
    u = (np.log(t)-value)/s
    
    risk = 1.0 - np.exp(-np.exp(u))
    
    return risk
