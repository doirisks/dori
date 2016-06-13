"""
example_c.py
by Ted Morin

contains example code for 8-year Diabtes Mellitus risks by beta coefficients and logistic model from
10.1001/archinte.167.10.1068
2007 Prediction of Incident Diabetes Mellitus in Middle Aged Adults
Framingham Heart Study
"""

from model_c import model

"Male Sex" "Age"  "Systolic BP" "Diastolic BP" "Height" "Weight" "HDL-C" "Triglycerides"  "Fasting Glucose"
"Parental History of DM" "Antihypertensive Medication Use"


toscore = []                                        # incomplete comments
toscore.append( [1,63,125,79,90,0,45,54,95,1,1] ) #m,63yrs,125sbp, 79dbp,72in,200lb, parent, treated
toscore.append( [0,61,124,85,80,0,45,85,105,0,0] ) #f,61yrs,124sbp, 85dbp, 71in,188lb,not parent, not treated
toscore.append( [1,55,118,76,92,0,45,75,85,0,1] ) #m, 55yrs,118sbp,76dbp,68in,210lb, 
toscore.append( [1,45,129,92,105,0,43,65,65,1,1] ) #m, 45, 129sbp, 92dbp,65in,257lb,
toscore.append( [1,71,125,84,88,0,49,55,45,0,1] ) #m, 71, 125sbp, 84dbp,74in,203lb,
toscore.append( [0,40,117,63,103,0,60,54,108,1,0] ) #f, 40, 117sbp, 75dbp,66in,246lb,
toscore.append( [0,43,127,69,90,0,59,71,64,1,0] ) #f, 43, 127sbp, 69dbp,63in,232lb,
toscore.append( [0,52,112,82,80,0,54,52,43,1,1] ) #f, 52, 125sbp, 82dbp,59in,160lb,
toscore.append( [0,61,141,101,90,0,43,44,51,0,0] ) #f, 61, 141sbp, 101dbp,68in,246lb,
toscore.append( [0,46,131,91,87,0,48,64,62,1,0] ) #f, 46yrs, 131sbp, 91dbp,70in,221lb,
toscore.append( [1,39,135,94,90,0,47,62,71,0,0] ) #m, 39yrs, 135sbp, 94dbp,71in,214lb,

scores = []
print "Risks"
for i in range(len(toscore)):
    scores.append( model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4], toscore[i][6], toscore[i][7],toscore[i][8],toscore[i][9],toscore[i][10]) )
    print "%.3f" % (float(scores[i])*100.)
