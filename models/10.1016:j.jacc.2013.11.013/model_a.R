# model_a.R
# by Ted Morin
# 
# contains a function to predict 2-year Stroke Risk for patients with new-onset AF using beta coefficients from
# 10.1016:j.jacc.2013.11.013
# 2014 Factors Associated With Major Bleeding Events: Insights From the ROCKET AF Trial
#
# All patient risk - some unpublished figures provided by DCRI
#
# single patient function expects parameters:
# "ismale"  "age"   "Diastolic BP"  "Hist of COPD" "Hist of Gastrointestinal Bleed" "Hist of Aspirin Use" "Hist of Anemia"
#           years        mg/dL        
#   bool   int/float    int/float         bool                     bool                       bool              bool

# accepts a dataframe argument
model_df = function(patients) {
  # a standardized order of the arguments
  arg_order = c(
    "female",
    "age",     #"per 5yr"
    "dbp1",    #per 5mmHg,  < 90mmHg
    "dbp2",    #per 5mmHg, >= 90mmHg
    "copd",
    "gihist",
    "asa",
    "anemia"
  );
  # # cox beta coefficients as derived from Table 6, warfarin censored (ln(HR))
  # c(
  #   -0.1984509387238383160134702620780444703996181488037109375,
  #   0.1570037488096646949298218487456324510276317596435546875,
  #   -0.08338160893905101345158215053743333555757999420166015625,
  #   0.246860077931525812022783838983741588890552520751953125,
  #   0.254642218373580753176810276272590272128582000732421875,
  #   0.63127177684185775685676844659610651433467864990234375,
  #   0.350656871613169329737758062037755735218524932861328125,
  #   0.63127177684185775685676844659610651433467864990234375
  # )
  
  # unpublished cox beta coefficients (courtesty of Dan Wojdyla at DCRI)
  betas = matrix(data = rep(c(
    -0.2006609093,
    0.0319323253,
    -0.016699566267,
    0.0490006936,
    0.2516815012,
    0.6321092535,
    0.3490772534,
    0.6307489711
  ),nrow(patients)), nrow = nrow(patients), byrow = TRUE, dimnames = list(c(), arg_order));
  
  # unpublished s0(2yrs) (courtesty of Dan Wojdyla at DCRI)
  s0 = 0.9467681553;
  
  # xbar value
  xbar = 1.066285222430056744968851489829830825328826904296875;
  
  # evaluate the sbp
  dbp1 = dbp2 = patients['dbp'];
  dbp1[which(dbp1 >= 90)] = 90;
  dbp2[which(dbp2 < 90 )] = 0;
  dbp2[which(dbp2 >= 90)] = dbp2[,'dbp'][which(dbp2 >= 90)] - 90;
  dbp = cbind(dbp1,dbp2);
  colnames(dbp) = c("dbp1", "dbp2");
  # adjust dbp representation in patients dataframe (also ensure correct ordering)
  patients = cbind(patients[arg_order[1:2]],dbp,patients[arg_order[5:8]]);

  # patients as a matrix
  patients_mat = as.matrix(patients);
  
  # dot the betas and the patient data 
  if (nrow(patients) == 1) {
    x = sum(betas[,arg_order] * patients_mat[,arg_order]);
  } 
  # support for multi-row dataframes here...
  #else {
    #x = rowSums(betas[,arg_order] * patients_mat[,arg_order]);
  #}
  
  # return the risk vector
  risk = 1 - s0**exp(x-xbar);
  
  patients = cbind(patients, x, risk);
  return(patients$risk)
}

# store the df model
save(model_df, file="model_df_a.Rdata")

# accepts a VECTOR argument
model = function (patient) {
  load("model_df_a.Rdata");
  ismale = patient[1];
  age    = patient[2];
  dbp    = patient[3];
  copd   = patient[4];
  gihist = patient[5];
  asa    = patient[6];
  anemia = patient[7];
  
  # convert "ismale" to "female"
  female = as.numeric(!ismale);
  
  # put the vectors into a dataframe
  patient.df = data.frame(female, age, dbp, copd, gihist, asa, anemia);
  
  # computes the risk
  risk = model_df(patient.df);
  return(risk[1])
}

# store the vector model
save(model, file = "model_a.Rdata")

# # code to calculate xbar from the a known data survival and data point
# risk = 0.14586
# s0   = 0.9467681553
# x    = 2.124844431770000152681632243911735713481903076171875
# xbar = x - log(log(1-risk)/log(s0))

# # test code 1
# testpat1 = c(1,70,70,0,0,0,0)
# result1 = model(testpat1)
# result1
# testpat2 = c(0,65,100,0,1,0,1)
# result2 = model(testpat2)
# result2

# # test code 2
# 1 - model(c(1, 70, 70, 0, 0, 0, 0)) # .94677
# 1 - model(c(0, 65,100, 0, 1, 0, 1)) # .85414
# 1 - model(c(1, 60,113, 1, 0, 0, 0)) # .89316
# 1 - model(c(0, 62, 85, 0, 1, 0, 0)) # .95049
# 1 - model(c(1, 95,120, 1, 1, 1, 1)) # .08714