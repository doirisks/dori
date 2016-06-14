"""
model_a.py
by Ted Morin

contains a function to predict 2-year incident Coronary Heart Disease risks using beta coefficients from 
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study

Uses Weibull model set to 2 years, no triglycerides for women

function expects parameters of
 "sex"   "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "alcohol consumption"
  m=T     years        mg/dL            mg/dL            mm Hg             oz/week
 bool    int/float    int/float       int/float        int/float          int/float

function expects parameters of (continued):
 "antihyp" "diabetic" "smoker" "menopaus"
   bool      bool       bool      bool
   
for men, menopaus = False
"""        

def model(ismale, age, totchol, hdlchol, sysBP, alcohol, antihyp, diabet, smoker, menopaus):
    import numpy as np
    
    # betas, s0's, xbars
    male_betas = [
        12.7868,            #Intercept
        -0.0405,            #Age
        -0.9494,            #ln(totchol/hdlchol)
        -1.0163,            #ln(sysBP)
        -0.0161,            #antihyp/sysBP interaction
        -0.4412,            #Diabetes
        -0.6042             #Smoker
    ]
    male_s = 0.7764
    
    female_betas = [
        20.4049,            #Intercept
        -0.0622,            #Age
        -3.8236,            #Menopause
        0.0717,             #Age * Menopause
        -0.8902,            #ln(totchol/hdlchol)
        -2.3607,            #ln(sysBP)
        -0.0097,            #antihyp/sysBP interaction
        -0.5734,            #Diabetes
        -0.4041,            #Smoker
        0.0461              #Alcohol (oz/wk)
    ]
    female_s = 0.7333
    
    #questionable alcohol conversion
    alcohol = alcohol * 3
    
    #prepare derived values
    if antihyp:
        if 110 < sysBP < 200:
            antihyp = antihyp * ((200 - sysBP) * float(sysBP -110)/100)
        else :
            antihyp = 0
    log_chol_ratio = np.log(float(totchol)/hdlchol)
    log_sysBP = np.log(sysBP)
    
    # a value for the intercept
    intercept = 1
    
    betas = None
    s0 = None
    if ismale :
        values = np.array([intercept,age, log_chol_ratio,log_sysBP,antihyp, diabet, smoker])
        betas = np.array(male_betas) 
        s = male_s
    else :
        menoage = age * menopaus
        values = np.array([intercept,age,menopaus,menoage,log_chol_ratio,log_sysBP,antihyp, diabet, smoker,alcohol])
        betas = np.array(female_betas)
        s = female_s
    # dot product
    value = np.dot(values, betas)
    
    # calculate using weibull regression model
    t = 2 # valid for 1 <= t <= 4, where t represent the number of years
    
    u = (np.log(t)-value)/s
    
    risk = 1.0 - np.exp(-np.exp(u))
    
    return risk
