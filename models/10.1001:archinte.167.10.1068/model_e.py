"""
model_e.py
by Ted Morin

contains a function to predict 8-year Diabtes Mellitus risks beta coefficients and logistic model from
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study

(Table 5, Complex Model 1)

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI" "Waist Circumf" "HDL-C" "Triglycerides"  "Fasting Glucose"
           years     mm Hg          mm Hg     kg/m^2       cm         mg/dL       mg/dL              mg/dL
  bool  int/float  int/float     int/float   int/float     i/f         i/f        i/f                i/f 

function expects parameters of (continued):
"Parental History of DM" "Antihypertensive Medication Use" "2-Hour Insulin Level" "Fasting Insulin Level" 
                                                                     mg/dL
    bool                            bool                            float/int            float/int
    
function expects parameters of (continued):
"C-reactive Protein Levels" 

        float/int           
"""  
# COMPLEX MODELS ARE INCOMPLETE: UNCHECKED + PERCENTILE VALUES NOT LISTED
def model(ismale,age,sbp,dbp,bmi,waistcirc,hdl,tri,glucose,parent,trtbp, ogtt, fastinsul, c_reactive):
    # imports
    import numpy as np

    # betas
    # derived from Odds Ratios in paper
    betas = np.array([
        −5.506,                     #Intercept
        0,                          #Age<50
        0.0086001718,               #Age 50-64
        -0.0809219076,              #Age >=65
        0.096910013,                #Male
        0.2121876044,               #Parental history of diabetes mellitus
        0,                          #BMI <25
        0.0334237555,               #BMI 25.0-29.9
        0.1205739312,               #BMI >=30
        0.1846914308,               #Blood pressure >130/85 mm Hg or receiving therapy
        0.367355921,                #HDL-C level <40 mg/dL in men or <50 mg/dL in women
        0.1613680022,               #Triglyceride level >=150 mg/dL
        0.1205739312,               #Waist circumference >88 cm in women or >102 cm in men
        0.7299742857,               #Fasting glucose level 100-126 mg/dL
        
        0.4578818967,               #2-Hour OGTT finding 140-200 mg/dL                     
        0.0899051114,               #Fasting insulin level >75th percentile                #TODO impossible?
        0.1553360375,               #C-reactive protein level >75th percentile             #TODO impossible?
        0,                          #Log Gutt insulin sensitivity index <25th percentile    # Not included
        0,                          #Log HOMA insulin resistance index >75th percentile     # Not included
        0                           #HOMA beta-cell index <25th percentile                  # Not included
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
        
    # Oral Glucose Tolerance Test
    if 140 <=  ogtt <= 200:
        values[14] = 1
        
    # Fasting insulin level
    crit_fastinsul = 1000000    # real value unknown TODO
    if fastinsul > crit_fastinsul:
        values[15] = 1
        
    # C-reactive protein
    crit_c_reactive = 1000000   # real value unknown TODO
    if c_reactive > crit_c_reactive:
        values[16] = 1
    
    # dot betas and values
    z = np.dot(betas,np.array(values))
    
    # calculate risk
    return 1.0 / (1 + np.exp(-z))
