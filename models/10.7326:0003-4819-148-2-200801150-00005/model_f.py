"""
model_f.py
by Ted Morin

contains a function to predict 4-year Incident Hypertension risks using point system from: 

2008 A Risk Score for Predicting Near-Term Incidence of Hypertension
Framingham Heart Study

Uses point system 4 year risks

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
        0.22,
        0.27,
        0.31,
        0.37,
        0.44,
        0.52,
        0.62,
        0.73,
        0.86,
        1.02,
        1.21,
        1.43,
        1.69,
        2.00,
        2.37,
        2.80,
        3.31,
        3.90,
        4.61,
        5.43,
        6.40,
        7.53,
        8.86,
        10.40,
        12.20,
        14.28,
        16.68,
        19.43,
        22.58,
        26.14,
        30.16,
        34.63,
        39.55,
        44.91,
        50.64,
        56.66,
        62.85,
        69.05,
        75.06,
        80.69,
        85.74
    ]
    
    return risk_percents[risk_index] / 100
