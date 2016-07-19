# Rrisk.R
# by Ted Morin
# 
# Handler for R risk requests
# 
# Expects: a repository directory, a model's DOI, its filename, and the model's arguments
# Output: a single risk score or "error[: error text]" on failure
# 
# ARGUMENT FORMAT:
# accepts only floats and integers
# floats must have a decimal point
# integers must NOT have a decimal point

# retrieve arguments
args = commandArgs(trailingOnly = TRUE);

# unpack arguments
repopath = args[1]
modelDOI = args[2]
modelDOI = sub('/', ':', modelDOI)
targetfile = args[3]
arguments = args[4:length(args)]

# move to the repository directory
if (dir.exists(repopath)) {
  setwd(repopath);
} else {
  stop("bad repository path");
}
# move to the DOI directory
if (dir.exists(modelDOI)){
  setwd(modelDOI);
} else {
  stop("DOI not found");
}
# load the requested model
if (file.exists(targetfile)) {
  load(targetfile)
} else {
  stop("model not found");
}

# print the score of the arguments given
springf(model(as.numeric(arguments)))
