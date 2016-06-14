"""
example_a.py
by Ted Morin

example code for
10.1001/archinte.159.11.1197
1999 Profile for Estimating Risk of Heart Failure

beta values from Table 3
(model b)

prints test output
"""

from model_b import model

#"ismale" "age" "LVH" "vital capacity" "heart rate" "systolic bp" "CHD" "valve disease" "diabetes" "cardiomegaly"
#"ismale" "age" "LVH" "heart rate" "systolic bp" "CHD" "valve disease" "diabetes" "BMI"
scores = []

scores.append( model(1,60,1,85,160,1,0,0,25) )
scores.append( model(1,47,0,72,118,1,0,1,26) )
scores.append( model(1,67,0,84,132,0,0,0,30) )
scores.append( model(0,46,0,103,106,0,1,0,24) )
scores.append( model(0,64,1,74,130,0,0,0,22) )
scores.append( model(0,57,0,55,115,0,1,0,27) )
scores.append( model(0,49,0,68,123,0,1,1,25) )

for score in scores:
    print "%.3f" % (score*100.)
