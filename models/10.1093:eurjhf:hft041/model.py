"""
model.py
by Ted Morin

contains a function to predict 10-year Atrial Fibrilation risks using beta coefficients from 
10.1093/eurjhf/hft041
2013 Risk Assessment for Incident Heart Failure in Individuals with Atrial Fibrillation

function expects parameters of
    "age"        "bmi"       "lvh"      "diabetic"      "sigmurm"        "pmi"
    years        kg/m^2  
  int/float    int/float      bool        bool            bool            bool 
  
functino uses the "Simple Model" cox regression
Spreadsheet equivalent can be found at http://www.framinghamheartstudy.org/risk-functions/spreadsheets/af_hf_risk_score_calculator.xls

"""        

def model(age, bmi, lvh, diabetic, sigmurm, pmi):
    import numpy as np
    
    # betas
    betas = np.array([
        0.0626,         # Age
        0.06204,        # BMI
        0.70814,        # Left Ventricular Hypertrophy
        0.63235,        # Diabetes
        0.60651,        # Significant Murmur
        3.58802,        # Prevalent Myocardial Infarction
        -0.03891        # Age times Prevalent Myocardial Infarction 
    ])
    
    s0 = 0.70509                # const is from  the spreadsheet, not from the paper
    xbar_value = 6.6663545052   # const is from  the spreadsheet, not from the paper
    # spreadsheet found at http://www.framinghamheartstudy.org/risk-functions/spreadsheets/af_hf_risk_score_calculator.xls
      
    values = [age, bmi, lvh, diabetic, sigmurm, pmi]
    # calculate derived values
    values.append(age*pmi)              # Age times prevalent Myocardial Infarction
    values = np.array(values)
    
    # dot product
    value = np.dot(values, betas)
    
    # calculate using cox regression model
    risk = 1.0 - np.power(s0, np.exp(value - xbar_value)); 
    # cap at .45, justified in paper: "we truncated the upper risk estimate at..."
    #if (risk > .45) : risk = .45         
    return risk
