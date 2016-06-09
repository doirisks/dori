"""
model_a.py
by Ted Morin

contains a function to predict 2-year incident Coronary Heart Disease risks using beta coefficients
for women (including triglycerides) from 
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study

Uses Weibull model set to 2 years
(Table 3)

function expects parameters of
 "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "alcohol consumption" "triglycerides"
 years        mg/dL            mg/dL            mm Hg             oz/week             mg/dL
int/float    int/float       int/float        int/float          int/float          int/float

function expects parameters of (continued):
 "antihyp" "diabetic" "smoker" "menopaus"
   bool      bool       bool      bool
   
N.B: Models c and d disagree for women with antihypertensives and high sysBP.
"""        

def model(age, totchol, hdlchol, sysBP, alcohol,triglyc, antihyp, diabet, smoker, menopaus):
    import numpy as np
    
    #questionable alcohol conversion
    alcohol = alcohol * 3
    
    # betas, s's
    betas = np.array([
        20.9717,            #Intercept
        -0.0621,            #Age
        -3.8522,            #Menopause
        0.0726,             #Age * Menopause
        -0.6256,            #ln(totchol/hdlchol)
        -2.2449,            #ln(sysBP)
        -0.098,             #antihyp/sysBP interaction
        -0.5243,            #Diabetes
        -0.3777,            #Smoker
        -0.2688,            #ln(triglycerides)
        0.0529             #Alcohol
    ])
    s = 0.7467
    
    #prepare derived values
    if antihyp:
        if 110 < sysBP < 200:
            antihyp = antihyp * ((200 - sysBP) * float(sysBP -110)/100)
        else :
            antihyp = 0
    log_chol_ratio = np.log(float(totchol)/hdlchol)
    log_sysBP = np.log(sysBP)
    menoage = age * menopaus
    triglyc = np.log(triglyc)
    
    # a value for the intercept beta
    intercept = 1
    
    
    values = np.array([intercept,age,menopaus,menoage,log_chol_ratio,log_sysBP,antihyp, diabet, smoker,triglyc,alcohol])
    # dot product
    value = np.dot(values, betas)
    #print value
    
    # calculate using weibull regression model
    t = 2 # valid for 1 <= t <= 4, where t represent the number of years
    
    u = (np.log(t)-value)/s
    
    risk = 1.0 - np.exp(-np.exp(u))
    
    return risk
