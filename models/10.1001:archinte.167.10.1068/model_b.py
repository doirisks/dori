"""
model_b.py
by Ted Morin

contains a function to predict 8-year Diabtes Mellitus risks beta coefficients and logistic model from
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study

(Table 3, by BMI only)

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI" "HDL-C" "Triglycerides"  "Fasting Glucose"
           years     mm Hg          mm Hg     kg/m^2   mg/dL       mg/dL              mg/dL
  bool  int/float  int/float     int/float   int/float  i/f        i/f                i/f 

function expects parameters of (continued):
"Parental History of DM" "Antihypertensive Medication Use"
    bool                            bool
"""  
def model(ismale,age,sbp,dbp,bmi,hdl,tri,glucose,parent,trtbp):
    # imports
    import numpy as np

    # betas
    # N.B. betas values copied from FHS website, derivation from Odds Ratios in paper gave slightly different values
    betas = np.array([
        -5.517,             #Intercept
        0,                  #Age <50        (reference)
        -0.018,             #Age 50-64
        -0.081,             #Age >=65
        -0.010,             #Male
        0.565,              #Parental history of diabetes mellitus
        0,                  #BMI <25        (reference)
        0.301,              #BMI 25-29.9
        0.92,               #BMI >=30
        0.498,              #BP > 130/85 or antihyp
        0.944,              #HDL-C lvl<40mg/dL (m) or <50mg/dL (f)
        0.575,              #Triglyceride >= 150mg/dL
        1.980              #Fasting glucose level 100-126mg/dL
    ])
    
    # determining factors:
    values = [0]*13
    
    values[0] = 1
    # age
    if age < 50:
        values[1] = 1
    elif age < 64 :
        values[2] = 1
    else :
        values[3] = 1
    
    # sex
    if ismale:
        values[4] = 1
    
    # parental history
    if parent:
        values[5] = 1
    
    # BMI
    if bmi < 25.:
        values[6] = 1
    elif bmi < 30.:
        values[7] = 1
    else :
        values[8] = 1
    
    # blood pressure
    if ((sbp >= 130.) or (dbp >= 85.) or trtbp) :
        values[9] = 1
    
    # HDL-C
    if ismale and hdl < 40:
        values[10] = 1
    elif (not ismale) and hdl < 50:
        values[10] = 1
    
    # Triglycerides
    if tri >= 150:
        values[11] = 1
    
    # Fasting glucose
    if glucose >= 100:
        values[12] = 1
    
    # dot betas and values
    z = np.dot(betas,np.array(values))
    
    # calculate risk
    return 1.0 / (1 + np.exp(-z))
    
