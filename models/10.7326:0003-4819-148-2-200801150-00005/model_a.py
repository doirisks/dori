"""
model_a.py
by Ted Morin

contains a function to predict 1-year Incident Hypertension risks using Weibull beta coefficients from: 
10.7326/0003-4819-148-2-200801150-00005
2008 A Risk Score for Predicting Near-Term Incidence of Hypertension
Framingham Heart Study

translated and adapted from from FHS online risk calculator's javascript
Uses Weibul model set to 1 year

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI"    "Smoking Status" "Parental with Hypert. History"
           years     mm Hg          mm Hg     kg/m^2 
  bool  int/float  int/float     int/float   int/float        bool                      int
"""        
def model(ismale,age,sbp,dbp,bmi,smoker,parentalht):
    # imports
    import numpy as np

    # betas and Weibull scale factor
    betas = np.array([
        22.949536,          #intercept
        -0.202933,          #female gender
        -0.156412,          #age
        -0.033881,          #bmi
        -0.05933,           #sbp
        -0.128468,          #dbp
        -0.190731,          #smoker
        -0.166121,          #parentalht 
        0.001624            #ageXdbp
    ])
    s = 0.876925
    
    # Fill in derived values
    ageXdbp = (age * dbp)
    
    # values 
    values = np.array([1, int(not ismale), age, bmi, sbp, dbp,smoker, parentalht, ageXdbp])
    
    # do computation
    betaSum = np.dot(betas, values)

    risk = 1.0 - np.exp( -np.exp(( np.log(1) - betaSum) / s))    
    #                                     ^only change between models a, b, and c

    return risk



