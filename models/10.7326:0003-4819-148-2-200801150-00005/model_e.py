"""
model_e.py
by Ted Morin

contains a function to predict 2-year Incident Hypertension risks using point system from: 

2008 A Risk Score for Predicting Near-Term Incidence of Hypertension
Framingham Heart Study

Uses point system 2 year risks

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI"    "Smoking Status" "Parental with Hypert. History"
           years     mm Hg          mm Hg     kg/m^2 
  bool  int/float  int/float     int/float   int/float        bool                      int
"""        
# models d, e, and f appear to differ substantially from a, b, and c in some ranges.
def model(ismale,age,sbp,dbp,bmi,smoker,parentalht):

    points = 0
    
    # systolic bp
    if sbp < 110:
        points += -4
    elif 110 <= sbp < 115 :
        points += 0
    elif 115 <= sbp < 120 :
        points += 2
    elif 120 <= sbp < 125 :
        points += 4
    elif 125 <= sbp < 130 :
        points += 6
    elif 130 <= sbp < 135 :
        points += 8
    else : # 135 <= sbp < 140, and if you are above that, then you are hypertensive, so...
        points += 10
    
    
    # sex
    if (ismale):
        pass
    else :
        points += 1
    
    # bmi
    if bmi >= 25:
        points += 1
    if bmi >= 30:
        points += 2
        
    # age and diastolic bp
    age_dbp_table = [
        [-8,-3,0,3,6],
        [-5,0,2,5,7],
        [-1,3,5,6,8],
        [3,5,7,8,9],
        [6,8,9,10,10],
        [10,11,11,11,11]
    ]
    age_cutoffs = [30,40,50,60,70]
    dbp_cutoffs = [70,75,80,85]
    age_index = 0
    for x in age_cutoffs:
        if age >= x:
            age_index += 1
    
    dbp_index = 0
    for x in dbp_cutoffs:
        if dbp >= x:
            dbp_index += 1
    
    points += age_dbp_table[age_index][dbp_index]
    
    # smoking
    if smoker:
        points += 1
    
    # parental hypertension
    points += parentalht
    
    # get score
    risk_index = points + 12
    risk_percents = [
        0.11,
        0.13,
        0.16,
        0.19,
        0.22,
        0.26,
        0.31,
        0.37,
        0.43,
        0.51,
        0.61,
        0.72,
        0.85,
        1.01,
        1.19,
        1.41,
        1.67,
        1.97,
        2.33,
        2.75,
        3.25,
        3.84,
        4.53,
        5.34,
        6.30,
        7.41,
        8.72,
        10.24,
        12.01,
        14.06,
        16.43,
        19.15,
        22.25,
        25.77,
        29.74,
        34.17,
        39.05,
        44.36,
        50.06,
        56.06,
        62.24
    ]
    
    return risk_percents[risk_index] / 100
