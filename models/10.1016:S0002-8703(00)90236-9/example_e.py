"""
example_a.py
by Ted Morin

contains example code for risk calculator in
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study
"""

from model_e import model


"ismale" "age" "total cholesterol" "hdl cholesterol" "systolic BP" "diabetic" "smoker"

toscore = [
    [1, 55,260,30,140,0,1],   #m, 55yrs, 260, 30hdl, 140, nondiab, smoker, 
    [1, 62,180,60,124,0,0],    #m, 62yrs, 180, 60hdl, 124, no conditions, 
    [1, 55,250,39,146,1,0],    #m, 55yrs, 250, 39hdl, 146, diab, nonsmoke, 
    [1, 55,165,46,118,0,0],    #m, 55yrs, 165, 46hdl, 118, nondiab, nonsmoker, 
    [0, 51,170,66,134,0,1],    #f, 51yrs, 170, 66hdl, 134, nondiab, smoker,
    [0, 61,220,43,144,1,0],    #f, 61yrs, 220, 43hdl, 144,diab, nonsmoker, 
    [0, 75,193,52,122,0,0]     #f, 75yrs, 193, 52hdl, 122,nondiab, nonsmoker, 
]
scores = []
for i in range(len(toscore)):
    scores.append(model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5],toscore[i][6]))
    print "%.3f" % (float(scores[i])*100.)
