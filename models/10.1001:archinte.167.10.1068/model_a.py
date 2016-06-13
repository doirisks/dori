"""
model_a.py
by Ted Morin

contains a function to predict 8-year Diabtes Mellitus risks using point system from 
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study

translated and adapted from from FHS online risk calculator's javascript

function expects parameters of:
"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "BMI" "HDL-C" "Triglycerides"  "Fasting Glucose"
           years     mm Hg          mm Hg     kg/m^2   mg/dL       mg/dL              mg/dL
  bool  int/float  int/float     int/float   int/float  i/f        i/f                i/f 

function expects parameters of (continued):
"Parental History of DM" "Antihypertensive Medication Use"
    bool                            bool
"""        

# original function name: DiabetesCalc
# returns a risk of 3% if risk is less than 3%
# returns a risk of 35% if risk is more than 35%
def model(ismale,age,sbp,dbp,bmi,hdl,tri,glucose,parent,trtbp):
    
    minPts = 10
    maxPts = 25
         
    riskTab = ([0]*10) + [
        3,          # 10
        4,          # 11
        4,          # 12
        5,          # 13
        6,          # 14
        7,          # 15
        9,          # 16
        11,          # 17
        13,          # 18
        15,          # 19
        18,          # 20
        21,          # 21
        25,          # 22
        29,          # 23
        33,          # 24
        35           # 25
    ]
    
    # points system
    
    points = 0
    
    if ( glucose >= 100 ):
        points += 10;
    
    if ( bmi >= 25.0):
        points += 2;
    
    if ( bmi >= 30.0 ):
        points += 3;
    
    if ismale :
        if hdl < 40.0: 
            points += 5
    else :
        if (hdl < 50.0):
            points += 5
    
    if ( parent ):
        points += 3
    
    if (tri >= 150):
        points += 3
    
    if ( (sbp >= 130) or (dbp >= 85) or (trtbp) ):
        points += 2
    
    # assumes risk is within a certain range
    riskLessThan = False        # unused
    riskGreaterThan = False     # unused
    if (points < minPts):
        points = minPts
        riskLessThan = True     # unused
    if (points > maxPts):
        points = maxPts
        riskGreaterThan = True  # unused
        
    # Risk from table
    return riskTab[points] * .01
