"""
example.py
by Ted Morin

contains example code for risk calculator in
10.1093/eurjhf/hft041
2013 Risk Assessment for Incident Heart Failure in Individuals with Atrial Fibrillation
"""

from model import model

"age, bmi, lvh, diabetic, sigmurm, prev mi"
toscore = [
    [89,21,0,0,0,0],    #89yrs, bmi 21, no conditions
    [40,23,0,1,0,0],    #36yrs, bmi 19, Diabetic
    [56,25,1,0,0,0]     #56yrs, bmi 25, Left Ventricular Hypertrophy
]
scores = []
for i in range(len(toscore)):
    scores.append(model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5]))


for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.)
