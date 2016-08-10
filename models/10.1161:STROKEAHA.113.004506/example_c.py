"""
example_c.py
by Ted Morin

contains example code for model c from
10.1161/STROKEAHA.113.004506
2014 Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban
"""

from model_c import model

# inputs: ['Age', 'Diastolic Blood Pressure', 'Platelets','Albumin','History of Coronary Heart Failure', 'History of Stroke or TIA', 'Asian Ethnicity', 'Black Ethnicity', 'Warfarin', 'Rivaroxaban']

# store patient data
toscore = [
    [66, 74, 322, 3.8, 1, 0, 0, 0, 0, 1],
    [85, 82, 205, 4.4, 0, 1, 0, 0, 1, 0],
    [65, 86, 176, 4.4, 0, 1, 0, 0, 1, 0],
    [69, 80, 346, 4.5, 1, 0, 0, 0, 1, 0],
    [81, 70, 200, 3.7, 1, 0, 0, 0, 1, 0]
]

# score data
scores = []
for patient in toscore:
    scores.append(model(*patient))

# show data
for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.)
    
"""
# correct beta values provided by Susanna Stevens
xbeta = [
    -1.87773,
    -0.23712,
    -0.56287,
    -1.64199,
    -0.83040
]
# for checking differences against SAS provided values
print (scores[0] - scores[1])- (xbeta[0] - xbeta[1])
print (scores[1] - scores[2])- (xbeta[1] - xbeta[2])
print (scores[2] - scores[3])- (xbeta[2] - xbeta[3])
print (scores[3] - scores[4])- (xbeta[3] - xbeta[4])
print
print (scores[4] - scores[0])- (xbeta[4] - xbeta[0])
print (scores[4] - scores[1])- (xbeta[4] - xbeta[1])
print (scores[4] - scores[2])- (xbeta[4] - xbeta[2])
print (scores[4] - scores[3])- (xbeta[4] - xbeta[3])
print
print scores[0], xbeta[0]
print
# calculating xbar_sum
xbar_sum = 0
for i in range(len(xbeta)):
    new_val = scores[i] - xbeta[i]
    print new_val
    xbar_sum += new_val
xbar_sum = xbar_sum/len(xbeta)
print xbar_sum
"""
