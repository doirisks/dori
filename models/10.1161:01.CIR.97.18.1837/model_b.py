"""
model_b.py
by Ted Morin

contains a function to predict 10-year Coronary Heart Disease risk using LDL cholesterol beta coefficients from 
10.1161:01.CIR.97.18.1837
1998 Prediction of Coronary Heart Disease Using Risk Factor Categories

(Table 7: Beta Coefficients Underlying CHD Prediction Sheets)

function expects parameters:
"ismale" "age"   "ldl cholesterol" "hdl cholesterol" "systolic BP" "diastolic BP" "diabetic" "smoker"
          years        mg/dL               mg/dL          mm Hg        mm Hg          
 bool   int/float    int/float           int/float      int/float    int/float       bool      bool


"""
def model(ismale,age,ldlchol,hdlchol,sysBP,diaBP,diabet,smoker):
    # imports
    import numpy as np
    
    # convert inputs to categories
    #TC = [categories...]
    TC = [0]*5
    if ldlchol >= 190:
        TC[4] = 1
    elif 160 <= ldlchol < 190:
        TC[3] = 1
    elif 130 <= ldlchol < 160:
        TC[2] = 1
    elif 100 <= ldlchol < 130:
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
        0.04808,            #Age
        -0.69281,           #LDLC
        0,                  #LDLC1
        0.00389,            #LDLC2
        0.26755,            #LDLC3
        0.56705,            #LDLC4
        0.48598,            #HDLC0
        0.21643,            #HDLC1
        0,                  #HDLC2
        -0.04710,           #HDLC3
        -0.34190,           #HDLC4
        -0.02642,           #BP0
        0,                  #BP1
        0.30104,            #BP2
        0.55714,            #BP3
        0.65107,            #BP4
        0.42146,            #Diabetes
        0.54377            #Smoker
    ]
    male_s0 = 0.90017
    male_xbar = 3.00069 #np.dot(np.array(male_betas),np.array(male_xbar_values))
    
    female_betas = [
        0.33994,            #Age
        -0.0027,            #Age^2
        -0.42616,           #LDLC0
        0,                  #LDLC1
        0.01366,            #LDLC2
        0.26948,            #LDLC3
        0.33251,            #LDLC4
        0.88121,            #HDLC0
        0.36312,            #HDLC1
        0.19247,            #HDLC2
        0,                  #HDLC3
        -0.35404,           #HDLC4
        -0.51204,           #BP0
        0,                  #BP1
        -0.03484,           #BP2
        0.28533,            #BP3
        0.50403,            #BP4
        0.61313,            #Diabetes
        0.29737            #Smoker
    ]
    female_s0 = 0.9628
    female_xbar = 9.914136  #np.dot(np.array(female_betas),np.array(female_xbar_values))

    
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


