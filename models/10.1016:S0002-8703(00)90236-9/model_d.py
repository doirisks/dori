"""
model_b.py
by Ted Morin

contains a function to predict 2-year incident Coronary Heart Disease risks using point system w/ triglycerides from
10.1016:S0002-8703(00)90236-9
2000 Primary and subsequent coronary risk appraisal: New results from The Framingham Study

(Figure 3) 

function expects parameters of
 "age"  "total cholesterol" "hdl cholesterol" "systolic BP" "alcohol consumption" "triglycerides"
 years        mg/dL            mg/dL            mm Hg             oz/week             mg/dL
int/float    int/float       int/float        int/float          int/float          int/float

function expects parameters of (continued):
 "antihyp" "diabetic" "smoker" "menopaus"
   bool      bool       bool      bool
   
N.B: Models c and d disagree for women with antihypertensives and high sysBP.
"""        

def model(age, totchol, hdlchol, sysBP, alcohol,triglyc, antihyp, diabet, smoker, menopaus):
    
    risk = 0.
    score = 0

    #questionable alcohol conversion
    alcohol = alcohol * 3

    if menopaus:
        if age >= 65: 
            score += 17
        elif 40 <= age < 18:
            score += 18
        else :
            score += 19
    else:
        agecutoffs = [40,45,50,55,60,65,70,1000]  #ridiculous values may cause errors
        age_scores = [0,1,3,4,6,7,9,10]
        for i in range(len(agecutoffs)):
            if age < agecutoffs[i]:
                score += age_scores[i]
                break
    
    if antihyp:
        sysBPcutoffs = [115,125,135,145,155,175,205,225,245,1000]  #ridiculous values may cause errors
        sysBP_scores = [  0,  2,  3,  4,  5,  6,  7,  8,  9,  10]
        for i in range(len(sysBPcutoffs)):
            if sysBP < sysBPcutoffs[i]:
                score += sysBP_scores[i]
                break
    else:
        sysBPcutoffs = [110,115,125,135,155,165,185,205,225,245,1000]  #ridiculous values may cause errors
        sysBP_scores = [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
        for i in range(len(sysBPcutoffs)):
            if sysBP < sysBPcutoffs[i]:
                score += sysBP_scores[i]
                break
    
    if diabet: score += 2
    if smoker: score += 2
    
    totchol_scores = [0]*17
    hdlcholcutoffs = [30,35,40,45,50,60,70,80,1000]  
    hdlchol_scores = [
        [3,4,4,4,4,4,4,4,5,5,5,5,5,5,5],
        [3,3,3,3,3,4,4,4,4,4,4,4,4,5,5],
        [2,3,3,3,3,3,3,3,4,4,4,4,4,4,4],
        [2,2,2,2,3,3,3,3,3,3,3,3,4,4,4],
        [2,2,2,2,2,2,3,3,3,3,3,3,3,3,3],
        [1,2,2,2,2,2,2,2,3,3,3,3,3,3,3],
        [1,1,1,1,1,2,2,2,2,2,2,2,2,3,3],
        [0,1,1,1,1,1,1,1,2,2,2,2,2,2,2],
        [0,0,0,0,1,1,1,1,1,1,1,2,2,2,2]
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
    
    triglyccutoffs = [25,95,195,355,10000]  #ridiculous values may cause errors
    triglyc_scores = [0, 2, 3, 4, 5]
    for i in range(len(triglyccutoffs)):
        if triglyc < triglyccutoffs[i]:
            score += triglyc_scores[i]
            break
    
    if menopaus:
        riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,100]
        risk_scores = [0,0,0,0,0,    0,0,0,0,0,   0,0,.01,.01,.03,    .05,.08,.14,.23,.37]
        for i in range(len(riskcutoffs)):
            if score < riskcutoffs[i]:
                risk = risk_scores[i]
                break
    else :
        riskcutoffs = [2,4,6,8,10,12,14,16,18,20,22,24,26,100]
        risk_scores = [0,0,0,0,0,  0,.01,.01,.02,.04,  .07,.12,.21,.34]
        for i in range(len(riskcutoffs)):
            if score < riskcutoffs[i]:
                risk = risk_scores[i]
                break
    
    #print score
    return risk
    
        
