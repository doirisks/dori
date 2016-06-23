"""
model_b.py
by Ted Morin

contains a function to predict 4-year risk of incident Intermittent Claudication using point system from
10.1161/01.CIR.96.1.44
1997 Intermittent Claudication: A Risk Profile From The Framingham Heart Study

function expects parameters of
'Sex' 'Age' 'Systolic BP' 'Diastolic BP' 'Cigarettes per day' 'Total Cholesterol' 'Diabetes' 'Previous CHD'
      years     mm Hg          mm Hg           n/day                mg/dL  
bool int/float int/float      int/float        int/float           int/float          bool        bool
"""
def model(ismale,age,sbp,dbp,cig,totchol,diab,chd):
    
    points = 0
    
    age_cutoffs = [50,55,60,65,70,75,80]
    for cutoff in age_cutoffs:
        if age >= cutoff:
            points += 1
    
    if ismale :
        points += 3
    
    if totchol < 170:
        pass
    elif totchol < 210:
        points += 1
    elif totchol < 250:
        points += 2
    elif totchol < 290:
        points += 3
    else : 
        points += 4
    
    if (sbp < 130) and (dbp < 85):
        points += 0
    elif (sbp < 140) and (dbp < 90):
        points += 1
    elif (sbp < 160) and (dbp < 100):
        points += 2
    else :
        points += 4
    
    if cig < 1:
        pass
    elif cig < 6:
        points += 1
    elif cig < 11:
        points += 2
    elif cig < 21:
        points += 3
    else :
        points += 4
    
    if diab :
        points += 5
    if chd :
        points += 5
    
    # look up risk
    if points >= 10:
        score = points - 10
    else :
        score = 0
    
    riskpercents = [1,1,1,2,2,2,3,3,4,5,6,7,8,10,11,13,16,18,21,24,28]
    
    risk = float(riskpercents[score]) / 100
    
    return risk
