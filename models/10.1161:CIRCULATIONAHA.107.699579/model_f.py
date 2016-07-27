"""
model_a.py
by Ted Morin

contains a function to predict 10-year CVD risks using point system from 
10.1161/CIRCULATIONAHA.107.699579
General Cardiovascular Risk Profile for Use in Primary Care
Framingham Heart Study

function expects parameters of
"ismale" "antihypertensive medication use" "age" "total colesterol" "HDL cholesterol" "SBD" "Smoking" "Diabetes"
                                           years      mg/dL               mg/dL       mm Hg
  bool                  bool             int/float   int/float          int/float   int/float  bool      bool
"""        
        
def model(ismale,antihyp,age,totchol,hdlchol,sbp, smoker,diabet):
    
    # count up points
    points = 0
    
    # depending on gender...
    if ismale: 
        # age
        age_cuts = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
        age_vals = [ 0,  2,  5,  6,  8, 10, 11, 12, 14, 15]
        i = -1
        for cut in age_cuts:
            if age >= cut:
                i += 1
        if age >= age_cuts[0]:
            points += age_vals[i]

        # hdlchol
        hdlchol_cuts = [ 0, 35, 45, 50, 60]
        hdlchol_vals = [ 2,  1,  0, -1, -2]
        i = -1
        for cut in hdlchol_cuts:
            if hdlchol >= cut:
                i += 1
        if hdlchol >= hdlchol_cuts[0]:
            points += hdlchol_vals[i]
        
        # totchol
        totchol_cuts = [  0, 160, 200, 240, 280]
        totchol_vals = [  0,   1,   2,   3,   4]
        i = -1
        for cut in totchol_cuts:
            if totchol >= cut:
                i += 1
        if totchol >= totchol_cuts[0]:
            points += totchol_vals[i]
        
        # sbp
        if (not antihyp):
            # sbp without
            sbp_cuts = [0, 120, 130, 140, 160]
            sbp_vals = [-2,  0,   1,   2,   3]
        else :
            # sbp with
            sbp_cuts = [0, 120, 130, 140, 160]
            sbp_vals = [0,   2,   3,   4,   5]
        i = -1
        for cut in sbp_cuts:
            if sbp >= cut:
                i += 1
        if sbp >= sbp_cuts[0]:
            points += sbp_vals[i]
            
        # smoker
        if smoker:
            points += 4
        
        # diabet
        if diabet:
            points += 3
        
        # risk
        risk_cuts = range(-3,18+1)
        risk_vals = [0.01, 0.011, 0.014, 0.016, 0.019, 0.023, 0.028, 0.033, 0.039, 0.047, 0.056, 0.067, 0.079, 0.094, 0.112, 0.132, 0.156, 0.184, 0.216, 0.254, 0.294, 0.3]
        i = 0
        for cut in risk_cuts:
            if points > cut:
                i += 1
        if i >= len(risk_vals):
            risk = risk_vals[-1]
        else :
            risk = risk_vals[i]
    
    # female
    else :
        # age
        age_cuts = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
        age_vals = [ 0,  2,  4,  5,  7,  8,  9, 10, 11, 12]
        i = -1
        for cut in age_cuts:
            if age >= cut:
                i += 1
        if age >= age_cuts[0]:
            points += age_vals[i]

        # hdlchol
        hdlchol_cuts = [ 0, 35, 45, 50, 60]
        hdlchol_vals = [ 2,  1,  0, -1, -2]
        i = -1
        for cut in hdlchol_cuts:
            if hdlchol >= cut:
                i += 1
        if hdlchol >= hdlchol_cuts[0]:
            points += hdlchol_vals[i]
        
        # totchol
        totchol_cuts = [  0, 160, 200, 240, 280]
        totchol_vals = [  0,   1,   3,   4,   5]
        i = -1
        for cut in totchol_cuts:
            if totchol >= cut:
                i += 1
        if totchol >= totchol_cuts[0]:
            points += totchol_vals[i]
        
        # sbp
        if (not antihyp):
            # sbp without
            sbp_cuts = [ 0, 120, 130, 140, 150, 160]
            sbp_vals = [-3,   0,   1,   2,   4,   5]
        else :
            # sbp with
            sbp_cuts = [ 0, 120, 130, 140, 150, 160]
            sbp_vals = [-1,   2,   3,   5,   6,   7]
        i = -1
        for cut in sbp_cuts:
            if sbp >= cut:
                i += 1
        if sbp >= sbp_cuts[0]:
            points += sbp_vals[i]
            
        # smoker
        if smoker:
            points += 3
        
        # diabet
        if diabet:
            points += 4
        
        # risk
        risk_cuts = range(-2,21+1)
        risk_vals = [0.01, 0.01, 0.012, 0.015, 0.017, 0.02, 0.024, 0.028, 0.033, 0.039, 0.045, 0.053, 0.063, 0.073, 0.086, 0.1, 0.117, 0.137, 0.159, 0.185, 0.215, 0.248, 0.285, 0.3]
        i = 0
        for cut in risk_cuts:
            if points > cut:
                i += 1
        if i >= len(risk_vals):
            risk = risk_vals[-1]
        else :
            risk = risk_vals[i]
    
    return risk
