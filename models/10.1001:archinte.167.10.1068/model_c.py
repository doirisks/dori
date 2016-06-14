"""
model_c.py
by Ted Morin

contains a function to predict 8-year Diabtes Mellitus risks beta coefficients and logistic model from
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study

(Table 3, by waist circumference only)

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "Waist Circumference" "HDL-C" "Triglycerides"  "Fasting Glucose"
           years     mm Hg          mm Hg     kg/m^2       cm         mg/dL      mg/dL              mg/dL
  bool  int/float  int/float     int/float   int/float     i/f        i/f         i/f                i/f

function expects parameters of (continued):
"Parental History of DM" "Antihypertensive Medication Use"
    bool                            bool
"""  
def model(ismale,age,sbp,dbp,waistcirc,hdl,tri,glucose,parent,trtbp):
    # imports
    import numpy as np

    # betas
    # derived from Odds Ratios in paper
    betas = np.array([
        -5.434,             #Intercept
        0,                  #Age <50        (reference)
        -0.06188,             #Age 50-64
        -0.18633,             #Age >=65
        0.08618,             #Male
        0.55962,              #Parental history of diabetes mellitus
        0.54812,              #BP > 130/85 or antihyp
        0.96317,              #HDL-C lvl<40mg/dL (m) or <50mg/dL (f)
        0.57661,              #Triglyceride >= 150mg/dL
        0.68310,             # Waist Circumference > 102cm (m) or >88cm (f)
        1.96991              #Fasting glucose level 100-126mg/dL
    ])
    
    # determining factors:
    values = [0]*11
    
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
    
    # blood pressure
    if ((sbp >= 130.) or (dbp >= 85.) or trtbp) :
        values[6] = 1
    
    # HDL-C
    if ismale and hdl < 40:
        values[7] = 1
    elif (not ismale) and hdl < 50:
        values[7] = 1
    
    # Triglycerides
    if tri >= 150:
        values[8] = 1
    
    # Waist Circumference
    if ismale and waistcirc > 102:
        values[9] = 1
    elif (not ismale) and waistcirc > 88:
        values[9] = 1
    
    # Fasting glucose
    if glucose >= 100:
        values[10] = 1
    
    # dot betas and values
    z = np.dot(betas,np.array(values))
    
    # calculate risk
    return 1.0 / (1 + np.exp(-z))
    
