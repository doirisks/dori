"""
model.py
by Ted Morin

contains a function to predict 4Y hear failure risk based on 
10.1001/archinte.159.11.1197
1999 Profile for Estimating Risk of Heart Failure

beta values from Table 2
(model a)

function expects parameters of
"ismale" "age" "LVH" "vital capacity" "heart rate" "systolic bp" "CHD" "valve disease" "diabetes" "cardiomegaly"
         years              L             bpm           mm Hg
 bool  int/float bool   int/float       int/float    int/float   bool       bool         bool         bool
LVH = Left Ventricular Hypertrophy
CHD = Congenital Heart Disease
"""

def model(ismale,age,lvh,vitcap,hrate,sbp,chd,valdis,diabetic,cardmegal):
    # imports
    import numpy as np
    
    # adjust for unusual units in beta values
    age = age #/ 10.                 # beta has units of 10Y
    vitcap = 100*vitcap #/ 1.          # beta has units of 100cL = 1L, but the example in the paper indicates the units used here
    hrate = hrate #/ 10.             # beta has units of 10bpm
    sbp = sbp #/ 20.                 # beta has units of 20mmHg
                                        # example in paper ignores tabular units for sbp, heart rate, and age...
    # betas
    male_betas = np.array([
        0.0313,             #Age
        0.8428,             #LVH
        -0.0030,            #Vital Capacity
        0.0144,             #Heart Rate
        0.0067,             #Systolic BP
        1.5333,             #CHD
        0.8868,             #Valve Disease
        0.2383,             #Diabetes
        0.7968             #Cardiomegaly
    ])
    male_interc = -7.3611
    
    female_betas = np.array([
        0.0216,             #Age
        1.0072,             #LVH
        -0.0087,            #Vital Capacity
        0.0092,             #Heart Rate
        0.0032,             #Systolic BP
        1.5358,             #CHD
        1.2454,             #Valve Disease
        1.4275,             #Diabetes
        0.4792,             #Cardiomegaly
        -0.9293            #Valve Disease and Diabetes      (not included in male betas)
    ])
    female_interc = -5.4997
    
    # gender decisions
    betas = None
    interc = None
    values = None
    if ismale:
        betas = male_betas
        interc = male_interc
        values = np.array([age,lvh,vitcap,hrate,sbp,chd,valdis,diabetic,cardmegal])
    else :
        betas = female_betas
        interc = female_interc
        values = np.array([age,lvh,vitcap,hrate,sbp,chd,valdis,diabetic,cardmegal,(valdis+diabetic)/2])
    
    # calculate risk
    x = interc + np.dot(betas,values)
    risk = 1./(1+np.exp(-x))               # straight from paper...?
    #risk = np.exp(x)/(1.+np.exp(x))         #online logistic regression tutorial
    
    return risk
