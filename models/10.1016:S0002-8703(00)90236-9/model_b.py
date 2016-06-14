"""
model_b.py
by Ted Morin

contains a function to predict 2-year incident Coronary Heart Disease risks using point system from
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study

(Figures 1 and 2) 

function expects parameters of
 "sex"   "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "alcohol consumption"
  m=T     years        mg/dL            mg/dL            mm Hg             oz/week
 bool    int/float    int/float       int/float        int/float          int/float

function expects parameters of (continued):
 "antihyp" "diabetic" "smoker" "menopaus"
   bool      bool       bool      bool
   
for men, menopaus = False
"""        

def model(ismale, age, totchol, hdlchol, sysBP, alcohol, antihyp, diabet, smoker, menopaus):
    
    risk = 0.
    score = 0
    
    #questionable alcohol conversion
    alcohol = alcohol * 3
    
    if ismale:
        
        agecutoffs = [40,45,50,55,60,65,70,1000]  #ridiculous values may cause errors
        age_scores = [0, 1, 3, 4, 6, 7, 9,10]
        for i in range(len(agecutoffs)):
            if age < agecutoffs[i]:
                score += age_scores[i]
                break
        """
        replacable_templatecutoffs = [40,45,50,55,60,65,70,1000]  #ridiculous values may cause errors
        replacable_template_scores = [0, 1, 3, 4, 6, 7, 9,10]
        for i in range(len(replacable_templatecutoffs)):
            if replacable_template < replacable_templatecutoffs[i]:
                score += replacable_template_scores[i]
                break
        """
        if antihyp:
            sysBPcutoffs = [110,115,125,135,145,155,215,1000]  #ridiculous values may cause errors
            sysBP_scores = [0, 1,2,3,4,5,6,6]
            for i in range(len(sysBPcutoffs)):
                if sysBP < sysBPcutoffs[i]:
                    score += sysBP_scores[i]
                    break
        else:
            sysBPcutoffs = [110,125,135,165,185,215,1000]  #ridiculous values may cause errors
            sysBP_scores = [0, 1, 2, 3, 4, 5, 6]
            for i in range(len(sysBPcutoffs)):
                if sysBP < sysBPcutoffs[i]:
                    score += sysBP_scores[i]
                    break
        
        if diabet: score += 3
        if smoker: score += 4
        
        totchol_scores = [0]*17
        hdlcholcutoffs = [30,35,40,45,50,60,70,80,1000]  
        hdlchol_scores = [
            [8,8,9,9,9,10,10,10,10,11,11,11,11,12,12],
            [7,7,7,8,8,8,9,9,9,9,10,10,10,10,11],
            [5,6,6,7,7,7,8,8,8,8,9,9,9,9,10],
            [5,5,5,6,6,6,7,7,7,8,8,8,8,9,9],
            [4,4,5,5,5,6,6,6,7,7,7,7,8,8,8],
            [3,4,4,4,5,5,5,6,6,6,6,7,7,7,7],
            [2,2,3,3,3,4,4,4,5,5,5,5,6,6,6],
            [1,1,2,2,2,3,3,3,4,4,4,4,5,5,5],
            [0,0,1,1,1,2,2,2,3,3,3,3,4,4,4]
        ]
        for i in range(len(hdlcholcutoffs)):
            if hdlchol < hdlcholcutoffs[i]:
                totchol_scores = hdlchol_scores[i]
                break
        
        totcholcutoffs = [170,180,190,200,210,220,230,240,250,260,270,280,290,300,1000]
        for i in range(len(totcholcutoffs)):
            if totchol < totcholcutoffs[i]:
                score += totchol_scores[i]
                break
        
        riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,100]
        risk_scores = [0,0,0,0,0,.01,.01,.01,.02,.03,.04,.06,.09,.12,.17, .24,.32,.43]
        for i in range(len(riskcutoffs)):
            if score < riskcutoffs[i]:
                risk = risk_scores[i]
                break
                
    else:
        
        if menopaus:
            if age >= 50: 
                score += 16
            else:
                score += 17
        else:
            agecutoffs = [40,45,50,55,60,65,70,1000]  #ridiculous values may cause errors
            age_scores = [0,1,3,4,6,7,9,10]
            for i in range(len(agecutoffs)):
                if age < agecutoffs[i]:
                    score += age_scores[i]
                    break
        
        if antihyp:
            sysBPcutoffs = [115,125,135,145,155,165,195,215,235,1000]  #ridiculous values may cause errors
            sysBP_scores = [  0,  2,  3,  4,  5,  6,  7,  8,  9,  10]
            for i in range(len(sysBPcutoffs)):
                if sysBP < sysBPcutoffs[i]:
                    score += sysBP_scores[i]
                    break
        else:
            sysBPcutoffs = [110,115,125,135,155,165,185,195,215,235,1000]  #ridiculous values may cause errors
            sysBP_scores = [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
            for i in range(len(sysBPcutoffs)):
                if sysBP < sysBPcutoffs[i]:
                    score += sysBP_scores[i]
                    break
        
        if diabet: score += 3
        if smoker: score += 2
        
        totchol_scores = [0]*17
        hdlcholcutoffs = [30,35,40,45,50,60,70,80,1000]  
        hdlchol_scores = [
            [5,5,5,5,6,6,6,6,6,7,7,7,7,7,7],
            [4,4,5,5,5,5,5,6,6,6,6,6,6,6,7],
            [3,4,4,4,4,5,5,5,5,5,5,6,6,6,6],
            [3,3,3,4,4,4,4,4,5,5,5,5,5,5,5],
            [2,3,3,3,3,3,4,4,4,4,4,5,5,5,5],
            [2,2,2,3,3,3,3,3,4,4,4,4,4,4,5],
            [1,1,2,2,2,2,2,3,3,3,3,3,3,4,4],
            [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],
            [0,0,0,1,1,1,1,1,2,2,2,2,2,2,3]
        ]
        for i in range(len(hdlcholcutoffs)):
            if hdlchol < hdlcholcutoffs[i]:
                totchol_scores = hdlchol_scores[i]
                break
        
        totcholcutoffs = [170,180,190,200,210,220,230,240,250,260,270,280,290,300,1000]
        for i in range(len(totcholcutoffs)):
            if totchol < totcholcutoffs[i]:
                score += totchol_scores[i]
                break
        
        if alcohol >= 6:
            score += -1
        
        if menopaus:
            riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,100]
            risk_scores = [0,0,0,0,0,    0,0,0,0,0,   .01,.01,.01,.02,.03,    .06,.11,.18,.31]
            for i in range(len(riskcutoffs)):
                if score < riskcutoffs[i]:
                    risk = risk_scores[i]
                    break
        else :
            riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,100]
            risk_scores = [0,0,0,0,0,  .01,.01,.02,.03,.05,   .09,.16,.27,.43]
            for i in range(len(riskcutoffs)):
                if score < riskcutoffs[i]:
                    risk = risk_scores[i]
                    break
                
    #print score
    return risk
    
        
