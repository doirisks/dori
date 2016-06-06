"""
example_a.py
by Ted Morin

example code for
10.1001/archinte.159.11.1197
1999 Profile for Estimating Risk of Heart Failure

beta values from Table 2
(model a)

prints test output
"""

from model_a import model

#"ismale" "age" "LVH" "vital capacity" "heart rate" "systolic bp" "CHD" "valve disease" "diabetes" "cardiomegaly"
scores = []

scores.append( model(1,60,1,2.5,85,160,1,0,0,1) )
scores.append( model(1,47,0,2.9,72,118,1,0,1,0) )
scores.append( model(1,67,0,3.2,84,132,0,0,0,1) )
scores.append( model(0,46,0,4.1,103,106,0,1,0,1))
scores.append( model(0,64,1,3.2,74,130,0,0,0,1) )
scores.append( model(0,57,0,3.7,55,115,0,1,0,1) )
scores.append( model(0,49,0,2.7,68,123,0,1,1,0) )

for score in scores:
    print "%.3f" % (score*100.)
