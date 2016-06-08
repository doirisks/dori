"""
model_d.py
by Ted Morin

contains a function to predict 10-year Coronary Heart Disease risk using LDL Cholesterol point system from
10.1161:01.CIR.97.18.1837
1998 Prediction of Coronary Heart Disease Using Risk Factor Categories

(Figures 3 and 4)

function expects parameters:
"ismale" "age"   "ldl cholesterol" "hdl cholesterol" "systolic BP" "diastolic BP" "diabetic" "smoker"
          years        mg/dL               mg/dL          mm Hg        mm Hg          
 bool   int/float    int/float           int/float      int/float    int/float       bool      bool


"""
def model(ismale,age,ldlchol,hdlchol,sysBP,diaBP,diabet,smoker):
    s = 0
    risk = None
    
    
    if ismale: #TODO correct female values to male values! female is complete
        # age
        s -= 1
        age_cutoffs = [35,40,45,50,55,60,65,70]
        age_deltas = [1,1,1,1,1,1,1,1]
        for i in range(len(age_cutoffs)):
            if age >= age_cutoffs[i]:
                s += age_deltas[i]
            else :
                break
                
        # LDL Cholesterol
        s -= 3
        ldlchol_cutoffs = [100,130,160,190]
        ldlchol_deltas = [3,0,1,1]
        for i in range(len(ldlchol_cutoffs)):
            if ldlchol >= ldlchol_cutoffs[i]:
                s += ldlchol_deltas[i]
            else :
                break

        # HDL Cholesterol
        s += 2
        hdlchol_cutoffs = [35,45,50,60]
        hdlchol_deltas = [-1,-1,0,-1]
        for i in range(len(hdlchol_cutoffs)):
            if hdlchol >= hdlchol_cutoffs[i]:
                s += hdlchol_deltas[i]
            else :
                break
        
        # blood pressure
        s -= 0
        sysbp_cutoffs = [120,130,140,160]
        diabp_cutoffs = [80,85,90,100]
        bp_deltas = [0,1,1,1]
        for i in range(len(sysbp_cutoffs)):
            if sysBP >= sysbp_cutoffs[i] or diaBP >= diabp_cutoffs[i]:
                s += bp_deltas[i]
            else :
                break
        
        if diabet:
            s += 2
        if smoker:
            s += 2
        
        # Risk
        risk = .01
        s_cutoffs = [-2,  0,  1,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]
        s_deltas = [.01,.01,.01,.02,.01,.02,.02,.03,.04,.04,.05,.06,.07,.07,.09]
        for i in range(len(s_cutoffs)):
            if s >= s_cutoffs[i]:
                risk += s_deltas[i]
            else :
                break
    
    else:
        # age
        s -= 9
        age_cutoffs = [35,40,45,50,55,60,65,70]
        age_deltas = [5,4,3,3,1,1,0,0]
        for i in range(len(age_cutoffs)):
            if age >= age_cutoffs[i]:
                s += age_deltas[i]
            else :
                break
                
        # LDL Cholesterol
        s -= 2
        ldlchol_cutoffs = [100,130,160,190]
        ldlchol_deltas = [2,0,2,0]
        for i in range(len(ldlchol_cutoffs)):
            if ldlchol >= ldlchol_cutoffs[i]:
                s += ldlchol_deltas[i]
            else :
                break

        # HDL Cholesterol
        s += 5
        hdlchol_cutoffs = [35,45,50,60]
        hdlchol_deltas = [-3,-1,-1,-2]
        for i in range(len(hdlchol_cutoffs)):
            if hdlchol >= hdlchol_cutoffs[i]:
                s += hdlchol_deltas[i]
            else :
                break
        
        # blood pressure
        s -= 3
        sysbp_cutoffs = [120,130,140,160]
        diabp_cutoffs = [80,85,90,100]
        bp_deltas = [3,0,2,1]
        for i in range(len(sysbp_cutoffs)):
            if sysBP >= sysbp_cutoffs[i] or diaBP >= diabp_cutoffs[i]:
                s += bp_deltas[i]
            else :
                break
        
        if diabet:
            s += 4
        if smoker:
            s += 2
        
        
        # Risk
        risk = .01
        s_cutoffs = [-1,  2,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17]
        s_deltas = [.01,.01,.01,.01,.01,.01,.01,.01,.02,.02,.02,.02,.03,.04,.03,.05]
        for i in range(len(s_cutoffs)):
            if s >= s_cutoffs[i]:
                risk += s_deltas[i]
            else :
                break
                
    return risk
