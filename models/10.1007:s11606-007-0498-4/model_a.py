"""
model_a.py
by Ted Morin

contains a function to predict ACS patient 30 Day Mortality risks using Cox Model from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
  
(Table 3)

function expects parameters of
    Age     Heart Rate      Weight     Creatin Clearance     Systolic BP     Diastolic BP
    float       float        float          float              float           float
    years      bpm           kg            mL/min              mmHg             mmHg
    
expected parameters continued...
    ST Segment Changes     Current Smoker     Enoxaparin User     Unfractionated Heparin User
            bool              bool                  bool                      bool
    
expected parameters continued...
    Baseline Rales      T-wave inversion on baseline ECG     Enrollment at a Latin American site     
        bool                            bool                            bool    
    
    
expected parameters continued...
    Prior Congestive Heart Failure   Prior Myocardial Infarction   Prior Percutaneous Coronary Intervention
            bool                                bool                            bool
            
expected parameters continued...
    Cardiac Biomarkers
            bool
"""     

def model(age, hrate, weight, crea_clear, sbp, dbp, stseg_change, smoke, enox, ufh, rales, twave, latin, hx_chf, hx_mi, hx_pci, card_bio):
    # imports
    import math
    
    # betas, s0, xbar_sum
    b = 0
    betas = [
        b,  # Increased Heart Rate
        b,  # Enoxaparin
        b,  # Unfractionated Heparin
        b,  # Prior CHF
        b,  # Increased Age
        b,  # Baseline Rales
        b,  # Increased weight <= 60kg
        b,  # Increased weight > 60kg
        b,  # CrCL <= 110ml/min
        b,  # CrCL > 110ml/min
        b,  # T-wave Inversion on Baseline ECG
        b,  # Increased SBP <= 145 mmHg
        b,  # Increased SBP > 145 mmHg
        b,  # Meets 2 inclusion criteria [as opposed to 3?]
        b,  # Prior MI
        b,  # Enrollment at Latin American Site
        b,  # Enoxaparin vs UFH - previous or never smokers
        b,  # Enoxaparin vs UFH - current smokers
        b,  # Increased DBP > 85 mmHg
        b   # Prior PCI
    ]
    s0 = 1          #TBD
    xbar_sum = 0    #TBD
    
    # derived variables
    
    if sbp <= 145 :                     # sbp
        sbp1 = sbp
        sbp2 = 0
    else :
        sbp1 = 145
        sbp2 = sbp - 145
    
    if crea_clear <= 110:               #crea_clear
        crea_clear1 = crea_clear
        crea_clear2 = 0
    else:
        crea_clear1 = 110
        crea_clear2 = crea_clear - 110
    
    if weight <= 60:                    # weight
        weight1 = weight
        weight2 = 0
    else:
        weight1 = 0
        weight2 = weight - 60
    
    criteria_met = 0                    # meets2
    if age >= 60 : criteria_met += 1
    if stseg_change: criteria_met += 1
    if not card_bio: criteria_met += 1
    if criteria_met == 2: 
        meets2 = 1
    else :
        meets2 = 0
    
    
    if smoke:
        nosmoke = 0
    else : 
        nosmoke = 1 
    
    # form the x vector
    xvals = [
        float(hrate) / 10.0,    
        enox,               
        ufh,                
        hx_chf,             
        float(age) / 10.0,  
        rales,              
        float(weight1) / 10.0,  #check this
        float(weight2) / 10.0,  #check this
        float(crea_clear1) / 10.0,      #check this
        float(crea_clear2) / 10.0,      #check this
        twave,              
        float(sbp1),        #check this
        float(sbp2),        #check this
        meets2,             #check this
        hx_mi,              
        latin,              
        enox * nosmoke,     #check this
        enox * smoke,       #check this
        float(dbp) / 10.0,  #check this
        hx_pci              
    ]
    
    # dot product
    xsum = 0
    for i in range(len(xvals)):
        xsum += xvals[i] * betas[i]
    xsum += xbar_sum
     
    risk = 1 - math.pow(s0,math.exp(xsum))
     
    return risk
