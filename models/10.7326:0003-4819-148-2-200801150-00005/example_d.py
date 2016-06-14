"""
example_d.py
by Ted Morin

contains example code for 1-year Hypertension risks using point system from
10.7326/0003-4819-148-2-200801150-00005
2008 A Risk Score for Predicting Near-Term Incidence of Hypertension
Framingham Heart Study
"""
# models d, e, and f appear to differ substantially from a, b, and c in some ranges.

from model_d import model

def bmi(inches,pounds):
    return 703.0704*pounds/(inches*inches)

toscore = []                    #ignore indices 6, 7, 8
toscore.append( [1,63,125,79,72,200,45,54,95,1,1] ) #m,63yrs,125sbp, 79dbp,72in,200lb, smoker, 1 parent
toscore.append( [0,61,124,85,71,188,45,85,105,0,0] ) #f,61yrs,124sbp, 85dbp, 71in,188lb, nosmokes, no parent
toscore.append( [1,55,118,76,68,210,45,75,85,0,1] ) #m, 55yrs,118sbp,76dbp,68in,210lb, nosmokes, 1 parent 
toscore.append( [1,45,129,92,65,257,43,65,65,1,1] ) #m, 45, 129sbp, 92dbp,65in,257lb, smokes, 1 parent
toscore.append( [1,71,125,84,74,203,49,55,45,0,1] ) #m, 71, 125sbp, 84dbp,74in,203lb, nosmokes, 1 parent
toscore.append( [0,40,117,63,66,246,60,54,108,1,2] ) #f, 40, 117sbp, 75dbp,66in,246lb, smokes,  both
toscore.append( [0,43,127,69,63,232,59,71,64,1,0] ) #f, 43, 127sbp, 69dbp,63in,232lb, smokes,  no parent
toscore.append( [0,52,112,82,59,160,54,52,43,1,1] ) #f, 52, 125sbp, 82dbp,59in,160lb, smokes, 1 parent
toscore.append( [0,61,141,101,68,246,43,44,51,0,1] ) #f, 61, 141sbp, 101dbp,68in,246lb, nosmokes, 1 parent
toscore.append( [0,46,131,91,70,221,48,64,62,1,2] ) #f, 46yrs, 131sbp, 91dbp,70in,221lb, smokes, both
toscore.append( [1,39,135,94,71,214,47,62,71,0,2] ) #m, 39yrs, 135sbp, 94dbp,71in,214lb, nosmokes, both

scores = []
print "Risks"
for i in range(len(toscore)):
    bmi_i = bmi(toscore[i][4],toscore[i][5])
    scores.append( model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],bmi_i, toscore[i][9],toscore[i][10]) )
    print "%.3f" % (float(scores[i])*100.)
