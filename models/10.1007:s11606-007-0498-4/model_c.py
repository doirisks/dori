"""
model_c.py
by Ted Morin

contains a function to predict ACS patient 1 Year Mortality risks after 30 Days using Cox Model from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
  
(Table 5)

function expects parameters of
    Male Sex    Age         Heart Rate    Weight at Baseline    Creatinine Clearance    Baseline Platelet  
      bool      float         float             float                  float                   float
                years           bpm              kg                   mL/min                  10^3/mm^3
    
expected parameters continued...
    Nadir Platelet   Hemoglobin    Current Smoker    Former Smoker    Atrial Fibrillation
        float           float           bool           bool               bool
       10^3/mm^3        g/dL           

expected parameters continued...
    Prior Coronary Artery Bypass Grafting    History of Diabetes    History of Angina   History of CHF
                bool                                bool                 bool               bool

expected parameters continued...
    ST Depression on Baseline ECG    Baseline Rales    Diagnostic Catheterization',
                bool                    bool                    bool
    
expected parameters continued...
    'Weight after 30 Days    Coronary Artery Bypass Grafting within 30 days    Use of Statin at 30 Days   
            float                               bool                                    bool
    
expected parameters continued...
    Percutaneous Coronary Intervention within 30 Days    Use of beta-blockers at 30 days'
                        bool                                        bool
"""     

def model(ismale, age, hrate, weight, crea_clear, plate, nadir_plate, hemo, curr_smoke, prev_smoke, af, hx_cabg, hx_diab, hx_ang, hx_chf, st_dep, rales, diag_cath, weight30, cabg30, stat30, pci30, beta30):
    # imports
    import math
    
    # betas, s0, xbar_sum
    b = 0
    betas = [
        b,  # Increased Hgb truncated above 15
        b,  # Atrial fibrillation/flutter
        b,  # Post-randomization CABG within 30 days of enrollment
        b,  # Male sex
        b,  # Baseline platelet beyond 200
        b,  # Use of statin at day 30
        b,  # Increased nadir platelet up to 200
        b,  # Increased creatinine clearance up to 110mL/min
        b,  # Increased heart rate
        b,  # Current Smoker
        b,  # History of CHF
        b,  # Post randomization PCI within 30 days of enrollment
        b,  # Increased age (years)
        b,  # Prior CABG
        b,  # Former Smoker
        b,  # History of Diabetes
        b,  # Use of beta-blockers at day 30
        b,  # Baseline rales
        b,  # ST depression on baseline ECG
        b,  # In-hospital post-randomization diagnostic catheterization
        b,  # Increased weight at day 30 (kg; baseline - 30day)
        b,  # Increased weight <= 60
        b,  # Increased weight > 60
        b,  # History of Angina
    ]
    s0 = 1          #TBD
    xbar_sum = 0    #TBD
    
    # derived variables
    
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
        
    weight30 = weight30 - weight        # weight30
    #if weight30 < 0: weight30 = 0
    
    if hemo > 15:                       # hemoglobin
        hemo = 15
    
    # form the x vector
    xvals = [
        float(hemo),
        af,                         #clear
        cabg30,                     #clear
        ismale,                     #clear
        float(plate)/ 10.0,
        stat30,                     #clear
        float(nadir_plate)/ 10.0,
        float(crea_clear1)/ 10.0,
        float(hrate)/ 10.0,
        curr_smoke,                 #clear
        hx_chf,                     #clear
        pci30,                      #clear
        float(age)/ 10.0,
        hx_cabg,                    #clear
        prev_smoke,                 #clear
        hx_diab,                    #clear
        beta30,                     #clear
        rales,                      #clear
        st_dep,                     #clear
        diag_cath,                  #clear
        float(weight30)/ 10.0,
        float(weight1)/ 10.0,
        float(weight2)/ 10.0,
        hx_ang                      #clear
    ]
    
    # dot product
    xsum = 0
    for i in range(len(xvals)):
        xsum += xvals[i] * betas[i]
    xsum += xbar_sum
     
    risk = 1 - math.pow(s0,math.exp(xsum))
     
    return risk
