#######################################################################################################################
# Ben Neely                       #                                               #
# Statistician                    #                                                                           #
######################################################################################################################
# Program: Score_new_data_in_R.R #
# Date:    Wednesday, Feb 10, 2016                               #
###################################################################################################################### 
load("trilogy_R_objects.Rdata")
attributes(trilogy_R_objects)
#new data entered programatically 
newdatt <- data.frame(cbind("CREATCN_IMP"=1.5,
                            "creatcn_imp85"=0.65, 
                            "N_PPIRD"=1,
                            "N_STATINRD"=1,
                            "NSTEMI"=1,
                            "KILLIP1_IMP"=1,
                            "AGEYR"=85,
                            "N_MHDIAB_IMP"=1,
                            "N_MHHYP_IMP"=1,
                            "N_MHCAD_IMP"=0,
                            "N_CANGIO_IMP"=0,
                            "SMOKE30_IMP"=1,
                            "N_MHHLP_IMP"=1,
                            "N_MHPAD_IMP"=0,                  
                            "N_MHPMI_IMP"=1,
                            "N_MHCHF_IMP"=0,
                            "N_MHPPCI_IMP"=1,
                            "N_MHPCABG_IMP"=0
))

#Only 1 row of data - this is all we need for our APP!, reconsider linear algebra if >1
same              <- intersect(names(newdatt),names(trilogy_R_objects$coef))
same2             <- intersect(names(trilogy_R_objects$referencePoints),names(trilogy_R_objects$coef))

# this calculation is done in accordance with the PMML Specification
r                 <- as.matrix(newdatt[same])                %*% as.matrix(trilogy_R_objects$coef[same])
s                 <- t(as.matrix(trilogy_R_objects$referencePoints[same2]))  %*% as.matrix(trilogy_R_objects$coef[same2])
H_t               <- trilogy_R_objects$cumulativeHazard*exp(r-s)
S_t               <- exp(-H_t)
final_scored      <- data.frame("risk"=1-S_t,"time"=trilogy_R_objects$time)
#At time 900:
tail(final_scored[which(final_scored$time<=900),],n=1)$risk