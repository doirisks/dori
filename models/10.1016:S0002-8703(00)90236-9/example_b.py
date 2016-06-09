"""
example_b.py
by Ted Morin

contains example code for risk calculator in
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study
"""

from model_b import model


"ismale" "age" "total cholesterol" "hdl cholesterol" "systolic BP" "diastolic BP" "diabetic" "smoker"
"sex"   "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "alcohol consumption"
"antihyp" "diabetic" "smoker" "menopaus" 
toscore = [
    [1, 55,260,30,140,5./3,1,0,1,0],   #m, 55yrs, 260, 30hdl, 140, 5oz/wk, antihyp, nondiab, smoker, no meno
    [1, 62,180,60,124,5./3,0,0,0,0],    #m, 62yrs, 180, 60hdl, 124, 5oz/wk, no conditions, no meno
    [1, 55,250,39,146,5./3,0,1,0,0],    #m, 55yrs, 250, 39hdl, 146, 5oz/wk, noantihyp, diab, nonsmoke, no meno
    [1, 55,165,46,118,5./3,0,0,0,0],    #m, 55yrs, 165, 46hdl, 118, 5oz/wk, noantihyp, nondiab, nonsmoker, no meno
    [0, 51,170,66,134,3./3,0,0,1,0],    #f, 51yrs, 170, 66hdl, 134, 3oz/wk, noantihyp, nondiab, smoker, no meno
    [0, 61,220,43,144,1./3,1,1,0,1],    #f, 61yrs, 220, 43hdl, 144, 1oz/wk, antihyp, diab, nonsmoker, meno
    [0, 75,193,52,122,2./3,1,0,0,1]     #f, 75yrs, 193, 52hdl, 122, 2oz/wk, antihyp, nondiab, nonsmoker, meno
]
scores = []
for i in range(len(toscore)):
    scores.append(model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5],toscore[i][6],toscore[i][7],toscore[i][8],toscore[i][9]))
    print "%.3f" % (float(scores[i])*100.)
