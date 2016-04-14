#######################################################################################################################
# Ben Neely                       #                                               #
# Statistician                    #                                                                           #
######################################################################################################################
# Program: CreateR_TRILOGYmodel_objects.R #
# Date:    Wednesday, Feb 10, 2016                               #
###################################################################################################################### 
library(ggplot2)
library(survival)
anal <- read.table("/sigma/db0029_trilogy/manu/02_secondary/trilo016-SponMIPrediction/10-data/50-model.csv",
header=TRUE,sep=",",na.strings="", dec=".", strip.white=TRUE)
analysis <- subset(anal,!is.na(anal$csponmi),
                   select=c(CREATCN_IMP,creatcn_imp85,AGEYR,ACSTPC2,N_MHDIAB_IMP,
                            N_MHPMI_IMP,N_MHCHF_IMP,N_MHHLP_IMP,N_CANGIO_IMP,N_MHPAD_IMP,N_MHHYP_IMP,
                            N_MHCAD_IMP,N_MHPPCI_IMP,KILLIP1_IMP,N_PPIRD,N_STATINRD,N_MHPCABG_IMP,
                            SMOKE30_IMP,HEMOGLBN_IMP,SBP_IMP,N_BETABLCK,
                            WGTKGBL_IMP,SEX,N_MHAF_IMP,TMI,csponmi
                            #These next variables are only for the full model
                            ,caucasian,HRT_IMP,N_ACEARB
                   ))
analysis$NSTEMI <- ifelse(analysis$ACSTPC2==2,1,0)
#Get functions needed to complete below.
require(survival)



#Create model for spontaneous mi
sponmod <- coxph(Surv(TMI,csponmi) ~  CREATCN_IMP + creatcn_imp85 + AGEYR + NSTEMI + 
                  N_MHDIAB_IMP + N_MHPMI_IMP + N_MHCHF_IMP + N_MHHLP_IMP + N_CANGIO_IMP + 
                  N_MHPAD_IMP + N_MHHYP_IMP + N_MHCAD_IMP + N_MHPPCI_IMP + KILLIP1_IMP + N_PPIRD +
                  N_STATINRD + N_MHPCABG_IMP + SMOKE30_IMP,data=analysis,x=TRUE)
########################################################################
# For this example, we will save enough info to get the 95% CI
########################################################################
trilogy_R_objects <- list("coef"=sponmod$coefficients,
                          "referencePoints"=sponmod$means,
                          "cumulativeHazard"=basehaz(sponmod)$hazard,
                          "time"=basehaz(sponmod)$time)
#for native R scoring example
save(trilogy_R_objects,file="trilogy_R_objects.Rdata")
#for restful api scoring example
save(trilogy_R_objects,file="../jugAPI/trilogy_R_objects.Rdata")
