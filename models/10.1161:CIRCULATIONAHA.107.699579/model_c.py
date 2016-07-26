"""
model_c.py
by Ted Morin

contains a function to predict 10-year Stroke risks using model from
10.1161/CIRCULATIONAHA.107.699579
General Cardiovascular Risk Profile for Use in Primary Care
Framingham Heart Study

function expects parameters of
"ismale" "antihypertensive medication use" "age" "total colesterol" "HDL cholesterol" "SBD" "Smoking" "Diabetes"
                                           years      mg/dL               mg/dL       mm Hg
  bool                  bool             int/float   int/float          int/float   int/float  bool      bool
"""        
        
def model(ismale,antihyp,age,totchol,hdlchol,sbp, smoke,diabet):
    
    # imports
    from model_a import model as model_a
    
    cvd = model_a(ismale,antihyp,age,totchol,hdlchol,sbp, smoke,diabet)
    
    male_calib_factor   = 0.1590
    female_calib_factor = 0.2385
    
    if ismale:
        return cvd * male_calib_factor
    else :
        return cvd * female_calib_factor
