"""
example_d.py
by Ted Morin

contains example code for model d from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
"""

from model_d import model

# inputs: 
#       Male Sex        Age     Creatinine Clearance     Weight     Hemoglobin      
#     Platelets           Nadir Platelets     Atrial Fibrillation
#    Statins at 30 Days              Coronary Artery Bypass Grafting within 30 days

# store patient data
toscore = [#                                                  #rales
    [1, 70, 80, 80, 12, 300, 200, 0, 0, 0]
]

# score data
scores = []
for patient in toscore:
    scores.append(model(*patient))

# show data
for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.)
