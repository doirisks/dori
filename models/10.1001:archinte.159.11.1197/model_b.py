"""
model.py
by Ted Morin

contains a function to predict 4Y hear failure risk based on 
10.1001/archinte.159.11.1197
1999 Profile for Estimating Risk of Heart Failure

beta values from Table 3
(model b)

function expects parameters of
"ismale" "age" "LVH" "heart rate" "systolic bp" "CHD" "valve disease" "diabetes" "BMI"
         years           bpm           mm Hg                                     kg/m^2?
 bool  int/float bool  int/float    int/float   bool       bool         bool    int/float
LVH = Left Ventricular Hypertrophy
BMI is listed as a bool in Table 3. Mistake?
"""

def model(ismale,age,lvh,hrate,sbp,chd,valdis,diabetic,bmi):
    # imports
    import numpy as np
    
    # adjust for unusual units in beta values
    age = age #/ 10.                 # beta has units of 10Y
    hrate = hrate #/ 10.             # beta has units of 10bpm
    sbp = sbp #/ 20.                 # beta has units of 20mmHg
                                        # example in paper ignores tabular units for sbp, heart rate, and age...
    
    # betas
    male_betas = np.array([
        0.0412,             #Age
        0.9026,             #LVH
        0.0166,             #Heart Rate
        0.00804,            #Systolic BP
        1.6079,             #CHD
        0.9714,             #Valve Disease
        0.2244              #Diabetes
    ])
    male_interc = -9.2087
    
    female_betas = np.array([
        0.0503,             #Age
        1.3402,             #LVH
        0.0105,             #Heart Rate
        0.00337,            #Systolic BP
        1.5549,             #CHD
        1.3929,             #Valve Disease
        1.3857,             #Diabetes
        0.0578,             #BMI
        -0.9860             #Valve Disease and Diabetes
    ])
    female_interc = -10.7988
    
    # gender decisions
    betas = None
    interc = None
    values = None
    if ismale:
        betas = male_betas
        interc = male_interc
        values = np.array([age,lvh,hrate,sbp,chd,valdis,diabetic])
    else :
        betas = female_betas
        interc = female_interc
        values = np.array([age,lvh,hrate,sbp,chd,valdis,diabetic,bmi,(valdis+diabetic)/2])
    
    # calculate risk
    x = interc + np.dot(betas,values)
    risk = 1./(1+np.exp(-x))               # straight from paper...?
    #risk = np.exp(x)/(1.+np.exp(x))         #online logistic regression tutorial
    
    return risk
