"""
model_a.py
by Ted Morin

contains a function to predict 2.5?-year Intracranial Bleeding risks using Cox Model from
10.1161/STROKEAHA.113.004506
2014 Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban
  
Note 1: "White/Other" Ethnicity is assumed if none is given

function expects parameters of
    Age     Diastolic Blood Pressure    Platelets   Albumin     History of Coronary Heart Failure
   float            float               float       float                   bool
   years            mmHg                10^9/L      g/dL

parameters continued...
History of Stroke or TIA     Asian Ethnicity    Black Ethnicity     Warfarin        Rivaroxaban
        bool                        bool            bool              bool              bool
"""     

def model(age, ):
    # imports
    import numpy as np
    
    

