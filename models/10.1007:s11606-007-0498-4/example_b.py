"""
example_b.py
by Ted Morin

contains example code for model b from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
"""

from model_b import model

# inputs: 
#    'Male Sex',    'Age',    'Heart Rate',     'Weight',    'Creatin Clearance',    'Current Smoker',
#    'Former Smoker',    "ST Depression on Baseline ECG",    'T-wave inversion on baseline ECG',    
#    'Baseline Rales',    'Prior Congestive Heart Failure',    'History of Diabetes',
#    'History of Peripheral Vascular Disease',      'Cardiac Biomarkers at Randomization', 
#    'Enoxaparin User',    'Unfractionated Heparin User',    'Killip Class'

# store patient data
toscore = [#                                       #  #
    [1, 66, 92, 72, 61, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 2],
    [1, 68,102, 65, 55, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 3],
    [1, 58, 88, 59, 50, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 4],
    [1, 74, 80, 50, 66, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 4],
    [1, 79, 79, 55, 48, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 3]
]

# score data
scores = []
for patient in toscore:
    scores.append(model(*patient))

# show data
for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.)
