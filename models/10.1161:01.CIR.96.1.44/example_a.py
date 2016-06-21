"""
example_a.py
by Ted Morin

contains example code for 1-year Hypertension risks using Weibull betas from
10.7326/0003-4819-148-2-200801150-00005
2008 A Risk Score for Predicting Near-Term Incidence of Hypertension
Framingham Heart Study
"""

from model_a import model

'Sex' 'Age' 'Systolic BP' 'Diastolic BP' 'Cigarettes per day' 'Total Cholesterol' 'Diabetes' 'Previous CHD'

                                                # disagrees with example in paper, but seems to be correct  
                                                # example in paper uses high-normal bp beta, whereas model_a
                                                # correctly uses high bp beta.

toscore = []     
toscore.append( [1,55,146,88,6,250,0,0] )       # example at end of paper
toscore.append( [1,55,144,81,10,248,.2,.34] )   # average 55-year old man (approximate: bp averages not used)
toscore.append( [1,70,146,89,30,240,1,0] )      # example used for point system in paper

scores = []
print "Risks"
for i in range(len(toscore)):
    scores.append( model(toscore[i][0],toscore[i][1],toscore[i][2],toscore[i][3],toscore[i][4],toscore[i][5],toscore[i][6],toscore[i][7]) )
    print "%.3f" % (float(scores[i])*100.)
