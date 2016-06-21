"""
example_b.py
by Ted Morin

contains example code for 1-year Hypertension risks using Weibull betas from
10.7326/0003-4819-148-2-200801150-00005
2008 A Risk Score for Predicting Near-Term Incidence of Hypertension
Framingham Heart Study
"""

from model_b import model

'Sex' 'Age' 'Systolic BP' 'Diastolic BP' 'Cigarettes per day' 'Total Cholesterol' 'Diabetes' 'Previous CHD'

toscore = []     
toscore.append( [1,55,146,88,6,250,0,0] ) 
toscore.append( [1,70,146,89,30,240,1,0] ) 

scores = []
print "Risks"
for i in range(len(toscore)):
    scores.append( model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5],toscore[i][6],toscore[i][7]) )
    print "%.3f" % (float(scores[i])*100.)
