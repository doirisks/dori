"""
model.py
by Ted Morin

contains a function to predict 10-year Atrial Fibrilation risks using beta coefficients from 
10.1016:S0140-6736(09)60443-8
2010 Development of a Risk Score for Atrial Fibrillation in the Community
Framingham Heart Study

translated and optimized from FHS online risk calculator's javascript

function expects parameters of
"Male Sex" "Age" "BMI" "Systolic BP" "Antihypertensive Medication Use" "PR Interval" "Sig. Murmur" "Prev Heart Fail"
          years  kg/m^2   mm Hg                                           mSec          
bool  int/float int/float int/float              bool                    int/float        bool        bool          
"""        

"""
    # originally part of the function, calculates xbar_value
    xbar_values = np.array([
        0.4464,                 # gender
        60.9022,                # age
        26.2861,                # bmi
        136.1674,               # sbp
        0.2413,                 # hrx
        16.3901,                # pr_intv
        0.0281,                 # vhd
        0.0087,                 # hxchf
        3806.9000,              # age2
        1654.6600,              # gender_age2
        1.8961,                 # age_vhd
        0.6100                  # age_hxchf
    ])
    xbar_value = np.dot(xbar_values,betas)      # this constant should be hard coded like s0!
                                                # (and now it is)
"""

        

def model(ismale, age, bmi, sbp, antihyp, pr_intv, sigmurm, phf):
    # convert seconds to milliseconds as used in regression
    pr_intv = pr_intv * 1000.0
    # inexplicable conversion
    pr_intv = pr_intv / 10.0        
    # this was done in the js, and the output seems much more realistic than otherwise, but it seems inexplicable!
    # perhaps the coefficient shown in FHS's website is erroneous? Or uses the wrong units? It is hard to say.
    
    import numpy as np
    
    # betas
    betas = np.array([
        1.994060,               #gender         
        0.150520,               #age            
        0.019300,               #bmi            Body Mass Index
        0.00615,                #sbp            Systolic Blood Pressure
        0.424100,               #hrx            Treatment for hypertension
        0.070650,               #pr_intv        PR interval
        3.795860,               #vhd            Significant Murmur
        9.428330,               #hxchf          Prevalent Heart Failure
        -0.000380,              #age2           age squared
        -0.000280,              #gender_age2    male gender times age squared
        -0.042380,              #age_vhd        age times murmur
        -0.123070               #age_hxchf      age times prevalent heart failure
    ])
    
    s0 = 0.96337                # "const is from  the spreadsheet"
    xbar_value = 10.785528582
    
    values = [ismale, age, bmi, sbp, antihyp, pr_intv, sigmurm, phf]
    # calculate derived values
    values.append(age*age)              # age squared
    values.append(ismale*age*age)       # gender times age squared
    values.append(sigmurm*age)          # age times significant murmur
    values.append(phf*age)
    values = np.array(values)
    
    # dot product
    value = np.dot(values, betas)
    
    print value,xbar_value
    # calculate using cox regression model
    risk = 1.0 - np.power(s0, np.exp(value - xbar_value)); 
    # cap at .3 
    #if (risk > .3) : risk = .3          # is this justified by the paper?
    return risk
