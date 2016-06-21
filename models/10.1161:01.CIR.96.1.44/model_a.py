"""
model_a.py
by Ted Morin

contains a function to predict 4-year risk of incident Intermittent Claudication using logistic model from
10.1161/01.CIR.96.1.44
1997 Intermittent Claudication: A Risk Profile From The Framingham Heart Study

function expects parameters of
'Sex' 'Age' 'Systolic BP' 'Diastolic BP' 'Cigarettes per day' 'Total Cholesterol' 'Diabetes' 'Previous CHD'
      years     mm Hg          mm Hg           n/day                mg/dL  
bool int/float int/float      int/float        int/float           int/float          bool        bool
"""
def model(ismale,age,sbp,dbp,cig,totchol,diab,chd):
    # imports
    import numpy as np                          # disagrees with example in paper, but seems to be correct:  
                                                # example in paper uses high-normal bp beta, whereas model_a
                                                # correctly uses high bp beta.
    
    # betas
    betas = np.array([
        -8.9152,               # Intercept
        0.5033,                # Male sex
        0.0372,                # Age
        0.2621,                # High normal
        0.4067,                # Stage 1 hypertension
        0.7977,                # Stage 2+ hypertension
        0.9503,                # Diabetes
        0.0314,                # Cigarettes/d
        0.0048,                # Cholesterol, mg/dL
        0.9939                # CHD
    ])
    
    # compute values 
    bp0 = 0             # high-normal
    bp1 = 0             # Stage 1 hypertension
    bp2 = 0             # Stage 2+ hypertension
    
    if (sbp < 130) and (dbp < 85):
        pass
    elif (sbp < 140) and (dbp < 90):
        bp0 = 1
    elif (sbp < 160) and (dbp < 100):
        bp1 = 1
    else :
        bp2 = 1
    
    # values 
    values = np.array([1,ismale,age,bp0,bp1,bp2,diab,cig,totchol,chd])
    
    # calculate risk
    x = np.dot(betas,values)
    risk = 1/(1 + np.exp(-x))
    
    return risk
