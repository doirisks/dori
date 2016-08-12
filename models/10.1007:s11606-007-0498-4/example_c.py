"""
example_c.py
by Ted Morin

contains example code for model c from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
"""

from model_c import model

# inputs: 
#   Male Sex    Age    Heart Rate    Weight at Baseline    Creatin Clearance    Baseline Platelet    
#   Nadir Platelet    Hemoglobin    Current Smoker    Former Smoker    Atrial Fibrillation    
#   Prior Coronary Artery Bypass Grafting    History of Diabetes    History of Angina    
#   ST Depression on Baseline ECG    Baseline Rales    Diagnostic Catheterization    Weight after 30 Days   
#   Coronary Artery Bypass Grafting within 30 days    Use of Statin at 30 Days    
#   Percutaneous Coronary Intervention within 30 Days    Use of beta-blockers at 30 days

# store patient data
toscore = [#                                                  #rales
    [1, 66, 92, 72, 61, 450, 140, 12, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 73, 1, 0, 0, 0],
    [1, 68,102, 65, 55, 550, 220,  8, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 62, 0, 1, 0, 0],
    [1, 58, 88, 59, 50, 450, 150, 16, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 61, 0, 1, 0, 0],
    [1, 74, 80, 50, 66, 350,  70,  9, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 55, 1, 0, 1, 1],
    [1, 79, 79, 55, 48, 850, 170, 14, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 57, 0, 1, 0, 1]
]

# score data
scores = []
for patient in toscore:
    scores.append(model(*patient))

# show data
for i in range(len(scores)):
    print "%.3f" % (float(scores[i])*100.)
