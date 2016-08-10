"""
example_a.py
by Ted Morin

contains example code for model a from
10.1161/STROKEAHA.113.004506
2014 Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban
"""

from model_a import model

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
