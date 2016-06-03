"""
example.py
by Ted Morin

contains example code for 10-year Atrial Fibrilation Risk calculator
10.1016:S0140-6736(09)60443-8
2010 Development of a Risk Score for Atrial Fibrillation in the Community
Framingham Heart Study
"""

from model import model

def bmi(inches,pounds):
    return 703.0704*pounds/(inches*inches)

def height_from(bmi,pounds):                # gives height in inches from bmi in kg/m^2 and weight in pounds
    import math
    return math.sqrt(703.0704*pounds/bmi)

"ismale, age, sbp, antihyp, pr_intv, sigmurm, phf"
scores = []
heights = []
scores.append( model(1,63,30,125,1,200,1,1) ) #m,63yrs,30bmi,125sbp, treated, 200pr_interval, sigm, phf
heights.append(height_from(30,170) )
scores.append( model(0,61,23,124,0,197,0,0) ) #f,61yrs,23bmi,124sbp,not treated, 197pr, no sigm, no phf
heights.append(height_from(23,170) )
scores.append( model(1,55,17,118,0,160,1,1) ) #m, 55yrs,17bmi,118sbp, not treated, 160pr, sigm, phf
heights.append(height_from(17,170) )
scores.append( model(1,45,20,129,1,180,1,1) ) #m, 45, 20bmi,129sbp, treated, 180pr, sigm, phf
heights.append(height_from(20,170) )
scores.append( model(1,71,19,125,0,193,0,1) ) #m, 71, 19bmi, 125sbp, notreated, 193pr, no sigm, phf
heights.append(height_from(19,170) )
scores.append( model(0,40,25,117,0,170,1,1) ) #f, 40, 25bmi, 117sbp, notreated,170pr, sigm, phf
heights.append(height_from(25,170) )
scores.append( model(0,43,22,127,1,195,1,0) ) #f, 43, 22bmi, 127sbp, treated, 195pr, sigm, no phf
heights.append(height_from(22,170) )
scores.append( model(0,52,22,112,1,145,1,1) ) #f, 52, 22bmi, 112sbp, treated, 145pr, sigm, phf
heights.append(height_from(22,170) )
scores.append( model(0,61,22,141,0,223,0,0) ) #f, 61, 22bmi, 141sbp,notreated, 223pr, no sigm, no phf
heights.append(height_from(22,170) )
scores.append( model(0,46,16,131,0,214,0,0) ) #f, 46yrs, 16bmi, 131sbp, notreated, 214pr, no sigm, no phf
heights.append(height_from(16,170) )
scores.append( model(1,39,15,135,0,174,0,0) ) #m, 39yrs, 15bmi, 135sbp, notreated, 174pr, no sigm, no phf
heights.append(height_from(15,170) )

print "Risks",'\t\t','Heights derived...'
for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.),'\t',"%.3f" % (float(heights[i]))
