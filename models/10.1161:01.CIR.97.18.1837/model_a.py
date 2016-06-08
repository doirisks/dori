"""
model_a.py
by Ted Morin

contains a function to predict 10-year Coronary Heart Disease risk using total cholesterol beta coefficients from 
10.1161:01.CIR.97.18.1837
1998 Prediction of Coronary Heart Disease Using Risk Factor Categories

(Table 6: Total Cholesterol Coefficients)

function expects parameters:
"ismale" "age" "total cholesterol" "hdl cholesterol" "systolic BP" "diastolic BP" "diabetic" "smoker"
          years        mg/dL               mg/dL          mm Hg        mm Hg          
 bool   int/float    int/float           int/float      int/float    int/float       bool      bool

function
"""
def model(ismale,age,totchol,hdlchol,sysBP,diaBP,diabet,smoker):
    # imports
    import numpy as np
    
    # convert inputs to categories
    #TC = [categories...]
    TC = [0]*5
    if totchol >= 280:
        TC[4] = 1
    elif 240 <= totchol < 280:
        TC[3] = 1
    elif 200 <= totchol < 240:
        TC[2] = 1
    elif 160 <= totchol < 200:
        TC[1] = 1
    else :
        TC[0] = 1
    # HDLC = [categories...]
    HDLC = [0] * 5
    if hdlchol >= 60:
        HDLC[4] = 1
    elif 50 <= hdlchol < 60:
        HDLC[3] = 1
    elif 45 <= hdlchol < 50:
        HDLC[2] = 1
    elif 35 <= hdlchol < 45:
        HDLC[1] = 1
    else :
        HDLC[0] = 1
    #Blood Pressure = [OPTIMAL, NORMAL, HIGH NORMAL, Stage I Hypertens, Stage II-IV Hypertens]
    BP = [0,0,0,0,0]                  
    if sysBP >= 160 or diaBP >=100:
        BP[4] = 1
    elif 140 <= sysBP < 160 or 90 <= diaBP < 100:
        BP[3] = 1
    elif 130 <= sysBP < 140 or 85 <= diaBP < 90:
        BP[2] = 1
    elif 120 <= sysBP < 130 or 80 <= diaBP < 85:
        BP[1] = 1
    else :
        BP[0] = 1
    
    
    
    # betas, s0's, xbars
    male_betas = [
        0.04826,            #Age
        -0.65945,           #TC0
        0,                  #TC1
        0.17692,            #TC2
        0.50539,            #TC3
        0.65713,            #TC4
        0.49744,            #HDLC0
        0.24310,            #HDLC1
        0,                  #HDLC2
        -0.05107,           #HDLC3
        -0.48660,           #HDLC4
        -0.00226,           #BP0
        0,                  #BP1
        0.28320,            #BP2
        0.52168,            #BP3
        0.61859,            #BP4
        0.42839,            #Diabetes
        0.52337             #Smoker
    ]
    male_s0 = 0.90015
    male_xbar = 3.0975#np.dot(np.array(male_betas),np.array(male_xbar_values))
    
    female_betas = [
        0.33766,            #Age
        -0.00268,           #Age^2
        -0.26138,           #TC0
        0,                  #TC1
        0.20771,            #TC2
        0.24385,            #TC3
        0.53513,            #TC4
        0.84312,            #HDLC0
        0.37796,            #HDLC1
        0.19785,            #HDLC2
        0,                  #HDLC3
        -0.42951,           #HDLC4
        -0.53363,           #BP0
        0,                  #BP1
        -0.06773,           #BP2
        0.26288,            #BP3
        0.46573,            #BP4
        0.59626,            #Diabetes
        0.29246             #Smoker
    ]
    female_s0 = 0.96246
    female_xbar = 9.92545  #np.dot(np.array(female_betas),np.array(female_xbar_values))

    
    #acconts for gender
    betas = None
    s0 = None
    xbar = None
    if ismale:
        betas = np.array(male_betas)
        s0 = male_s0
        xbar = male_xbar
        # builds a numpy array of the values
        values = np.array([age] + TC + HDLC + BP + [diabet,smoker])
    else:
        betas = female_betas
        s0 = female_s0
        xbar = female_xbar
        # builds a numpy array of the values
        values = np.array([age,age*age] + TC + HDLC + BP + [diabet,smoker])
    
    # dots the betas and the values
    value = np.dot(betas,values)
    
    # returns the cox-calculated value
    return 1. - np.power(s0,np.exp(value - xbar))


