"""
model_f.py
by Ted Morin

contains a function to predict 2-year subsequent Coronary Heart Disease risks using point system from
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study

(Figures 4 and 5) 

function expects parameters of
 "sex"   "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "diabetic" "smoker"
  m=T     years        mg/dL            mg/dL            mm Hg      
 bool    int/float    int/float       int/float        int/float      bool       bool  
"""        

def model(ismale, age, totchol, hdlchol, sysBP, diabet, smoker):
    
    risk = 0.
    score = 0
    
    if ismale:
        
        agecutoffs = [40,45,50,55,60,65,70,1000]  #ridiculous values may cause errors
        age_scores = [ 0, 1, 3, 4, 6, 7, 9,10]
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
        
        if diabet: score += 4
        
        totchol_scores = [0]*15
        hdlcholcutoffs = [30,35,40,45,50,60,70,80,1000]  
        hdlchol_scores = [
            [10,11,11,12,12,13,13,13,14,14,15,15,15,16,16],
            [9,9,10,10,11,11,11,12,12,13,13,13,14,14,14],
            [7,8,8,9,9,10,10,10,11,11,12,12,12,13,13],
            [6,7 ,7,8,8,9,9,9,10,10,10,11,11,11,12],
            [5,6,6,7,7,7,8,8,9,9,9,10,10,10,11],
            [4,5,5,6,6,7,7,7,8,8,8,9,9,9,10],
            [3,3,4,4,5,5,5,6,6,6,7,7,7,8,8],
            [1,2,2,3,3,4,4,4,5,5,5,6,6,6,7],
            [0,1,1,2,2,2,3,3,4,4,4,5,5,5,6]
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
        
        riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,100]
        risk_scores = [0.03,0.04,0.04,0.05,0.06,0.07,0.08,0.09,0.11,0.13,0.14,0.17,0.19,0.22,0.25,0.29]
        for i in range(len(riskcutoffs)):
            if score < riskcutoffs[i]:
                risk = risk_scores[i]
                break
                
    else:
        agecutoffs = [40,45,50,55,60,65,70,1000]  #ridiculous values may cause errors
        age_scores = [ 0, 1, 2, 3, 4, 5, 6,   7]
        for i in range(len(agecutoffs)):
            if age < agecutoffs[i]:
                score += age_scores[i]
                break
        
        sysBPcutoffs = [110,115,125,135,145,155,165,185,195,215,225,245,1000]  #ridiculous values may cause errors
        sysBP_scores = [  0,  1,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,  13]
        for i in range(len(sysBPcutoffs)):
            if sysBP < sysBPcutoffs[i]:
                score += sysBP_scores[i]
                break
        
        if diabet: score += 8
        if smoker: score += 4
        
        totchol_scores = [0]*17
        hdlcholcutoffs = [30,35,40,45,50,60,70,1000]  
        hdlchol_scores = [
            [10,11,11,12,12,13,13,14,14,14,15,15,15,16,16],
            [9,9,10,10,11,11,12,12,12,13,13,13,14,14,14],
            [7,8,8,9,9,10,10,11,11,11,12,12,12,13,13],
            [6,7,7,8,8,9,9,9,10,10,11,11,11,12,12],
            [5,6,6,7,7,8,8,8,9,9,9,10,10,10,11],
            [4,5,5,6,6,7,7,7,8,8,9,9,9,10,10],
            [3,3,4,4,5,5,5,6,6,7,7,7,8,8,8],
            [1,2,2,3,3,4,4,4,5,5,6,6,6,7,7],
            [0,1,1,2,2,2,3,3,4,4,4,5,5,5,6]
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
        
        riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,100]
        risk_scores = [0.01,0.01,0.01,0.01,0.02,0.02,0.02,0.03,0.03,
                        0.04,0.05,0.05,0.07,0.08,0.09,0.11,0.13,0.16,0.19,0.22]

        for i in range(len(riskcutoffs)):
            if score < riskcutoffs[i]:
                risk = risk_scores[i]
                break
                
    #print score
    return risk
    
        
