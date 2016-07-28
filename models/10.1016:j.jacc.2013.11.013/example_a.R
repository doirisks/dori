# exapmle_a.R
# by Ted Morin
# 
# contains an example code for predicting 10-year Stroke Risk using point system from
# 10.1016:j.jacc.2013.11.013
# 2014 Factors Associated With Major Bleeding Events: Insights From the ROCKET AF Trial

# load the function
load('model_a.Rdata')

# create test patients
testpat1 = c(1,70, 70,0,0,0,0)
testpat2 = c(0,65,100,0,1,0,1)

# calculate single patient risk scores
model(testpat1)
model(testpat2)