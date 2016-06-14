"""
model_d.py
by Ted Morin

contains a function to predict 8-year Diabtes Mellitus risks beta coefficients and logistic model from
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study

(Table 3, by BMI and Waist Circumference)

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI" "Waist Circumf" "HDL-C" "Triglycerides"  "Fasting Glucose"
           years     mm Hg          mm Hg     kg/m^2       cm         mg/dL       mg/dL              mg/dL
  bool  int/float  int/float     int/float   int/float     i/f         i/f        i/f                i/f 

function expects parameters of (continued):
"Parental History of DM" "Antihypertensive Medication Use"
    bool                            bool
"""  
def model(ismale,age,sbp,dbp,bmi,waistcirc,hdl,tri,glucose,parent,trtbp):
    # imports
    import numpy as np

    # betas
    # derived from Odds Ratios in paper
    betas = np.array([
        -5.363,             #Intercept
        0.0,                #Age < 50
        -0.0202027073175,   #Age 50-64
        -0.0943106794712,   #Age >= 65
        0.0487901641694,    #Male
        0.576613364304,     #Parent History
        0.0,                #BMI < 25
        0.190620359609,     #BMI 25-30
        0.620576487725,     #BMI >= 30
        0.482426149244,     #BP
        0.93609335917,      #HDL-C
        0.559615787935,     #Triglycerides
        0.350656871613,     #Waist Circumference
        1.96850998097      #Fasting Glucose
    ])
    
    # determining factors:
    values = [0]*14
    
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
    
    # Waist Circumference
    if ismale and waistcirc > 102:
        values[12] = 1
    elif (not ismale) and waistcirc > 88:
        values[12] = 1
    
    # Fasting glucose
    if glucose >= 100:
        values[13] = 1
    
    # dot betas and values
    z = np.dot(betas,np.array(values))
    
    # calculate risk
    return 1.0 / (1 + np.exp(-z))
