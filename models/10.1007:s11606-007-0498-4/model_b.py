"""
model_b.py
by Ted Morin

contains a function to predict ACS patient 1 Year Mortality risks using Cox Model from
10.1007/s11606-007-0498-4
2008 Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial
  
(Table 4)

function expects parameters of
    Male Sex    Age    Heart Rate     Weight    Creatinine Clearance      Current Smoker    Former Smoker
      bool     float     float        float             float                   bool            bool
               years      bpm           kg              mL/min
    
expected parameters continued...
    ST Depression on Baseline ECG      T-wave inversion on baseline ECG    Baseline Rales    
                bool                            bool                            bool
    
expected parameters continued...
    Prior Congestive Heart Failure    History of Diabetes    History of Peripheral Vascular Disease
            bool                            bool                            bool    

expected parameters continued...
    Cardiac Biomarkers at Randomization       Enoxaparin User      Unfractionated Heparin User
                bool                                bool                    bool
                
expected parameters continued...
    Killip Class
       integer
"""     

def model(ismale, age, hrate, weight, crea_clear, curr_smoke, prev_smoke, st_dep, twave, rales, hx_chf, hx_diab, hx_pvd, card_bio, enox, uhf, killip):
    # imports
    import math
    
    # betas, s0, xbar_sum
    b = 0
    betas = [
        b,  # Male Sex
        b,  # Increased Creatinine Clearance <= 110 mL/min
        b,  # Increased Creatinine Clearance > 110 mL/min
        b,  # Increased Heart Rate
        b,  # Current Smoking Status
        b,  # Former Smoking Status
        b,  # History of CHF
        b,  # Increased Age
        b,  # History of Diabetes
        b,  # Baseline Rales
        b,  # ST depression on baseline ECG
        b,  # Increased Weight <= 60
        b,  # Increased Weight > 60
        b,  # History of PVD
        b,  # Killip Class 3 or 4
        b,  # No positive biomarkers at randomization
        b,  # T-wave inversion on baseline ECG
        b   # Enoxaparin vs UFH
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
    
    if killip == 3 or killip == 4:
        killip = 1
    else :
        killip = 0
    
    if not card_bio:                    # card_bio
        no_card_bio = 1
    else :
        no_card_bio = 0
    
    # form the x vector
    xvals = [
        ismale,            
        float(crea_clear1) / 10.0,       
        float(crea_clear2) / 10.0,       
        float(hrate)/ 10.0,         
        curr_smoke,        
        prev_smoke,        
        hx_chf,            
        float(age)/ 10.0,           #check this
        hx_diab,           
        rales,             
        st_dep,            
        float(weight1)/ 10.0,       #check this
        float(weight2)/ 10.0,       #check this
        hx_pvd,            
        killip,            
        no_card_bio,       
        twave,             
        enox               
    ]
    
    # dot product
    xsum = 0
    for i in range(len(xvals)):
        xsum += xvals[i] * betas[i]
    xsum += xbar_sum
     
    risk = 1 - math.pow(s0,math.exp(xsum))
     
    return risk
