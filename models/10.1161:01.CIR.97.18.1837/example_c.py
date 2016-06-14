"""
example_a.py
by Ted Morin

contains example code for risk calculator in
10.1161:01.CIR.97.18.1837
1998 Prediction of Coronary Heart Disease Using Risk Factor Categories

function expects parameters:
"ismale" "age" "total cholesterol" "hdl cholesterol" "systolic BP" "diastolic BP" "diabetic" "smoker"
          years        mg/dL               mg/dL          mm Hg        mm Hg          
 bool   int/float    int/float           int/float      int/float    int/float       bool      bool
"""

from model_c import model


toscore = [
    [1, 62,180,60,124,83,0,0],    #m, 62yrs, 180, 60hdl, 124, 83, 0, 0
    [1, 55,250,39,146,88,1,0],    #m, 55yrs, 250, 39hdl, 146, 88, diab, nonsmoke
    [1, 55,165,46,118,78,0,0],    #m, 55yrs, 165, 46hdl, 118, 78, nondiab, nonsmoker
    [0, 51,170,66,134,91,0,1],    #f, 51yrs, 170, 66hdl, 134, 91, nondiab, smoker
    [0, 61,220,43,144,99,1,0],    #f, 61yrs, 220, 43hdl, 144, 99, diab, nonsmoker
    [0, 75,193,52,122,83,0,0]     #f, 75yrs, 193, 52hdl, 122, 83, nondiab, nonsmoker
]
scores = []
for i in range(len(toscore)):
    scores.append(model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5],toscore[i][6],toscore[i][7]))
    print "%.3f" % (float(scores[i])*100.)
