"""
example_d.py
by Ted Morin

contains example code for risk calculator in
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study
"""

from model_d import model



"age"  "total cholesterol" "hdl cholesterol" "systolic BP" "alcohol consumption" "triglycerides"
"antihyp" "diabetic" "smoker" "menopaus" 
toscore = [
    [51,170,66,134,3./3,265,0,0,1,0],    #f, 51yrs, 170, 66hdl, 134, 3oz/wk,265tri, noantihyp, nondiab, smoker, no meno
    [61,220,43,144,1./3,265.59,1,1,0,1], #f, 61yrs, 220, 43hdl, 144, 1oz/wk,265.59, antihyp, diab, nonsmoker, meno
    [75,193,52,122,2./3,265.59,1,0,0,1], #f, 75yrs, 193, 52hdl, 122, 2oz/wk,265.59, antihyp, nondiab, nonsmoker, meno
    [51,170,66,134,3./3,280,0,0,1,0],    #f, 51yrs, 170, 66hdl, 134, 3oz/wk,280tri, noantihyp, nondiab, smoker, no meno
    [61,220,43,144,1./3,234,1,1,0,1],    #f, 61yrs, 220, 43hdl, 144, 1oz/wk,234tri, antihyp, diab, nonsmoker, meno
    [75,193,52,122,2./3,299,1,0,0,1],     #f, 75yrs, 193, 52hdl, 122, 2oz/wk,299tri, antihyp, nondiab, nonsmoker, meno
    [61,220,43,144,1./3,234,1,0,0,1],    #f, 61yrs, 220, 43hdl, 144, 1oz/wk,234tri, antihyp, nondiab, nonsmoker, meno
    [61,220,43,144,1./3,234,1,0,1,1],    #f, 61yrs, 220, 43hdl, 144, 1oz/wk,234tri, antihyp, nondiab, smoker, meno
    [61,220,43,144,1./3,234,1,1,0,0],    #f, 61yrs, 220, 43hdl, 144, 1oz/wk,234tri, antihyp, diab, nonsmoker, nomeno
    [49,220,43,144,1./3,234,1,1,0,1],    #f, 49yrs, 220, 43hdl, 144, 1oz/wk,234tri, antihyp, diab, nonsmoker, meno
    [61,180,62,144,1./3,234,1,0,0,1],    #f, 61yrs, 180, 62hdl, 144, 1oz/wk,234tri, antihyp, diab, nonsmoker, meno
]
scores = []
for i in range(len(toscore)):
    scores.append(model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5],toscore[i][6],toscore[i][7],toscore[i][8],toscore[i][9]))
    print "%.3f" % (float(scores[i])*100.)
