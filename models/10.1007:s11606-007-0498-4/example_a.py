"""
example_a.py
by Ted Morin

contains example code for model a from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
"""

from model_a import model

# inputs: [    'Age',    'Heart Rate',     'Weight',    'Creatin Clearance',    'Systolic BP',    'Diastolic BP',    "ST Segment Changes", 'Current Smoker',    'Enoxaparin User',    'Unfractionated Heparin User',     'Baseline Rales',    'T-wave inversion on baseline ECG',    'Enrollment at a Latin American site',    'Prior Congestive Heart Failure',    'Prior Myocardial Infarction',    'Prior Percutaneous Coronary Intervention',    'Cardiac Biomarkers']

# store patient data
toscore = [#                        #  #
    [66, 92, 72, 61, 120, 80, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [68,102, 65, 55, 141, 80, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [58, 88, 59, 50, 150, 80, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [74, 80, 50, 66, 120, 80, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [79, 79, 55, 48, 120, 80, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
]

# score data
scores = []
for patient in toscore:
    scores.append(model(*patient))

# show data
for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.)
