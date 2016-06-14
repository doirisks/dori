"""
model_f.py
by Ted Morin

contains a function to predict 8-year Diabtes Mellitus risks beta coefficients and logistic model from
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study

(Table 5, Complex Model 2)

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI" "Waist Circumf" "HDL-C" "Triglycerides"  "Fasting Glucose"
           years     mm Hg          mm Hg     kg/m^2       cm         mg/dL       mg/dL              mg/dL
  bool  int/float  int/float     int/float   int/float     i/f         i/f        i/f                i/f 

function expects parameters of (continued):
"Parental History of DM" "Antihypertensive Medication Use" "Gutt Insulin Sensitivity Index"
                                                                        
    bool                            bool                               float/int
"""  
# COMPLEX MODELS ARE INCOMPLETE: UNCHECKED + PERCENTILE VALUES NOT LISTED
def model(ismale,age,sbp,dbp,bmi,waistcirc,hdl,tri,glucose,parent,trtbp, guttinsul):
    # imports
    import numpy as np

    # betas
    # derived from Odds Ratios in paper
    betas = np.array([
        −5.427,                     #Intercept
        0,                          #Age<50
        -0.0043648054,                #Age 50-64
        -0.0915149811,                #Age >=65
        0.0492180227,                #Male
        0.2380461031,                #Parental history of diabetes mellitus
        0,                          #BMI <25
        0.0681858617,                #BMI 25.0-29.9
        0.2552725051,                #BMI >=30
        0.1461280357,                #Blood pressure >130/85 mm Hg or receiving therapy
        0.3384564936,                #HDL-C level <40 mg/dL in men or <50 mg/dL in women
        0.1760912591,                #Triglyceride level >=150 mg/dL
        0.096910013,                #Waist circumference >88 cm in women or >102 cm in men
        0.7259116323,                #Fasting glucose level 100-126 mg/dL
        0,                          #2-Hour OGTT finding 140-200 mg/dL                      # Not Included
        0,                          #Fasting insulin level >75th percentile                 # Not Included
        0,                          #C-reactive protein level >75th percentile              # Not Included
        0.357934847,                #Log Gutt insulin sensitivity index <25th percentile    # TODO impossible?
        0,                          #Log HOMA insulin resistance index >75th percentile     # Not Included
        0,                          #HOMA beta-cell index <25th percentile                  # Not Included
    ])
    
    # determining factors:
    values = [0]*20
    
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
        
    # Log GUTT insulin sensitivity index
    guttinsul = np.log(guttinsul)
    crit_guttinsul = -1000000        # real value not known TODO
    if guttinsul < crit_guttinsul:
        values[17] = 1
    
    # dot betas and values
    z = np.dot(betas,np.array(values))
    
    # calculate risk
    return 1.0 / (1 + np.exp(-z))
