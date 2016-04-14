/*--------------------------------------+-----------------------|
|  Ben Neely                            | (919) 668-6834        |
|  Duke Clinical Research Institute     | ben.neely@dm.duke.edu |
|                                       | NP.4561               |
|---------------------------------------+-----------------------|
|  Program:   acc_aha_201310yrCVDrisk.sas                       |
|                                                               |
|  Date:  Thursday, May 22, 2014 12:54:10                       |
|--------------------------------------------------------------*/

/* Apply the 2013 ACC AHA 10 year CVD Risk algorithm as published in:
DC Goff, LLoyd-Jones DM, 2013 ACC/AHA Guideline on the Assessment of Cardiovascular Risk: A Report of the 
American College of Cardiology/American Heart Association Task Force on Practice Guidelines, CIRC 11.12.2013
*/
%macro acc_aha_201310yrCVDrisk( DSin=,					/* Data Set In - the data to apply the algorithm to */
								DSout=,					/* Data Set Out - the data to return with predicted Goff 2013 ACC/AHA Guidline Risk Estimates */
								MALE=,					/* MALE, 1=Yes / 0=No */
								nonHispAA=,				/* Non-Hispanic Afican American 1=Yes / 0=No*/
								AGE=,					/* Age in years [40,79] ORIGINAL VALUE - NOT TRANSFORMED! */
								SBP=,					/* Systolic Blood Pressure (mmHG) ORIGINAL VALUE - NOT TRANSFORMED! */
								TRTBP=,					/* Treatment for Hypertension 1=Yes / 0=No */
								TCL=,					/* Total Cholesterol (mg/DL) ORIGINAL VALUE - NOT TRANSFORMED! */
								HDL=,					/* HDL Cholesterol (mg/DL)ORIGINAL VALUE - NOT TRANSFORMED! */
								DIAB=,					/* Diabetic Indicator 1=Yes / 0=No */
								SMOKE=					/* Current Smoker 1=Yes / 0=No */
							  );
/*Load up the parameter estimates as seen on Table A. */
data EffectEstimates;
/*First Row */
	&MALE.=1; &nonHispAA.=0;
	lAGEbeta=12.344; lAGEsqbeta=0; lTCLbeta=11.853; lAGExlTCLbeta=-2.664; lHDLbeta=-7.99; lAGExlHDLbeta=1.769; lTRTSBPbeta=1.797; lTRTSBPxlAGEbeta=0;
	lUNTRTSBPbeta=1.764; lUNTRTSBPxlAGEbeta=0; SMOKEbeta=7.837; SMOKExlAGEbeta=-1.795; DIABbeta=0.658; DERIVATION_LP_MEAN=61.18; baselineSurvivalFx=0.9144;
output;
/*Second Row*/
	&MALE.=1; &nonHispAA.=1;
	lAGEbeta=2.469; lAGEsqbeta=0; lTCLbeta=0.302; lAGExlTCLbeta=0; lHDLbeta=-0.307; lAGExlHDLbeta=0; lTRTSBPbeta=1.916; lTRTSBPxlAGEbeta=0;
	lUNTRTSBPbeta=1.809; lUNTRTSBPxlAGEbeta=0; SMOKEbeta=0.549; SMOKExlAGEbeta=0; DIABbeta=0.645; DERIVATION_LP_MEAN=19.54; baselineSurvivalFx=0.8954;
output;
/*Third Row*/
	&MALE.=0; &nonHispAA.=0;
	lAGEbeta=-29.799; lAGEsqbeta=4.884; lTCLbeta=13.54; lAGExlTCLbeta=-3.114; lHDLbeta=-13.578; lAGExlHDLbeta=3.149; lTRTSBPbeta=2.019; lTRTSBPxlAGEbeta=0;
	lUNTRTSBPbeta=1.957; lUNTRTSBPxlAGEbeta=0; SMOKEbeta=7.574; SMOKExlAGEbeta=-1.665; DIABbeta=0.661; DERIVATION_LP_MEAN=-29.18; baselineSurvivalFx=0.9665;
output;
/*Fourth Row*/
	&MALE.=0; &nonHispAA.=1;
	lAGEbeta=17.114; lAGEsqbeta=0; lTCLbeta=0.94; lAGExlTCLbeta=0; lHDLbeta=-18.92; lAGExlHDLbeta=4.475; lTRTSBPbeta=29.291; lTRTSBPxlAGEbeta=-6.432;
	lUNTRTSBPbeta=27.82; lUNTRTSBPxlAGEbeta=-6.087; SMOKEbeta=0.691; SMOKExlAGEbeta=0; DIABbeta=0.874; DERIVATION_LP_MEAN=86.61;baselineSurvivalFx=0.9533;
output;
run;
/*************************************************************
Comment 1: Let the real work begin - derive the risk estimates
**************************************************************/
data &DSout.;
   length lAGEbeta lAGEsqbeta lTCLbeta lAGExlTCLbeta lHDLbeta lAGExlHDLbeta lTRTSBPbeta lTRTSBPxlAGEbeta 8;
   length lUNTRTSBPbeta lUNTRTSBPxlAGEbeta SMOKEbeta SMOKExlAGEbeta DIABbeta DERIVATION_LP_MEAN baselineSurvivalFx 8;
   if _N_ = 1 then do;
      /* load SMALL data set into the hash object */
     declare hash h(dataset: "effectestimates");
      /* define SMALL data set variable K as key and S as value */
      h.defineKey("&MALE.","&nonHispAA.");
      h.defineData('lAGEbeta','lAGEsqbeta','lTCLbeta','lAGExlTCLbeta','lHDLbeta','lAGExlHDLbeta','lTRTSBPbeta','lTRTSBPxlAGEbeta','lUNTRTSBPbeta','lUNTRTSBPxlAGEbeta','SMOKEbeta',
				   'SMOKExlAGEbeta','DIABbeta','DERIVATION_LP_MEAN','baselineSurvivalFx');
      h.defineDone();
      /* avoid uninitialized variable notes */
      call missing(lAGEbeta,lAGEsqbeta,lTCLbeta,lAGExlTCLbeta,lHDLbeta,lAGExlHDLbeta,lTRTSBPbeta,lTRTSBPxlAGEbeta,lUNTRTSBPbeta,lUNTRTSBPxlAGEbeta,SMOKEbeta,SMOKExlAGEbeta,DIABbeta,
				   DERIVATION_LP_MEAN,baselineSurvivalFx);
   end;
set &DSin.;
rc = h.find();
/* First, all continuous variables were natural log transformed */
l&age. = log(&age.);
l&sbp. = log(&sbp.);
l&tcl. = log(&tcl.);
l&hdl. = log(&hdl.);
UNTRTBP = (&TRTBP.=0);
if &TRTBP.=. then UNTRTBP=.;
/*Get the linear predictors from this model stratified by sex and race/ethnicity */
if &male.=0 & &nonHispAA.=0 then do;
	lp = (lAGEbeta*l&age.) + (lAGEsqbeta*(l&age.)**2) + (lTCLbeta*l&tcl.) + (lAGExlTCLbeta*(l&age.*l&tcl.)) + (lHDLbeta*l&hdl.) + (lAGExlHDLbeta*(l&age.*l&hdl.)) +
	     (lTRTSBPbeta*(&TRTBP.*l&SBP.)) + (lUNTRTSBPbeta*(UNTRTBP*l&SBP.)) + (SMOKEbeta*&smoke.) + (SMOKExlAGEbeta*(&smoke.*l&age.)) + (DIABbeta*&diab.);
end;
if &male.=0 & &nonHispAA.=1 then do;
	lp = (lAGEbeta*l&age.) + (lTCLbeta*l&tcl.) + (lHDLbeta*l&hdl.) + (lAGExlHDLbeta*(l&age.*l&hdl.)) +
	     (lTRTSBPbeta*(&TRTBP.*l&SBP.)) + (lTRTSBPxlAGEbeta*(&TRTBP.*l&SBP.*l&AGE.)) + (lUNTRTSBPbeta*(UNTRTBP*l&SBP.)) + (lUNTRTSBPxlAGEbeta*(UNTRTBP*l&SBP.*l&AGE.)) +
		 (SMOKEbeta*&smoke.) + (SMOKExlAGEbeta*(&smoke.*l&age.)) + (DIABbeta*&diab.);
end;
else if &male.=1 & &nonHispAA.=0 then do;
	lp = (lAGEbeta*l&age.) + (lTCLbeta*l&tcl.) + (lAGExlTCLbeta*(l&age.*l&tcl.)) + (lHDLbeta*l&hdl.) + (lAGExlHDLbeta*(l&age.*l&hdl.)) +
	     (lTRTSBPbeta*(&TRTBP.*l&SBP.)) + (lUNTRTSBPbeta*(UNTRTBP*l&SBP.)) + (SMOKEbeta*&smoke.) + (SMOKExlAGEbeta*(&smoke.*l&age.)) +(DIABbeta*&diab.);
end;
else if &male.=1 & &nonHispAA.=1 then do;
	lp = (lAGEbeta*l&age.) + (lTCLbeta*l&tcl.) + (lHDLbeta*l&hdl.) + (lTRTSBPbeta*(&TRTBP.*l&SBP.)) + (lUNTRTSBPbeta*(UNTRTBP*l&SBP.)) + (SMOKEbeta*&smoke.) + (DIABbeta*&diab.);
end;
/* Calculate the 10 year risk */
ACC_AHA_201310yrCVDrisk = (1 - baselineSurvivalFx**(exp(lp-DERIVATION_LP_MEAN)));
if (&age.<40 | &age.>79) then do;
	ACC_AHA_201310yrCVDrisk =.; /*Do not apply the risk algorithm outside of these age ranges based on manuscript*/ 
	lp=.;
end;
drop rc lAGEbeta lAGEsqbeta lTCLbeta lAGExlTCLbeta lHDLbeta lAGExlHDLbeta lTRTSBPbeta lTRTSBPxlAGEbeta lUNTRTSBPbeta lUNTRTSBPxlAGEbeta SMOKEbeta SMOKExlAGEbeta DIABbeta 
	 DERIVATION_LP_MEAN baselineSurvivalFx l&age. l&sbp. l&tcl. l&hdl. UNTRTBP;
label lp = 'Linear Predictors from the 2013 ACC AHA Geoff CVD 10 year Risk Algorithm'
      ACC_AHA_201310yrCVDrisk = '10 year risk estimate from the 2013 ACC AHA Geoff CVD 10 year Risk Algorithm';
run;
%mend;
/**********************************************************************************************
Comment 2: For testing/playing with macro use the following input data set / macro invocation
**********************************************************************************************/
/* Four patient examples were given in table A, these can be used to ensure that the algorithm 
   is implemented correctly or to examine its use */
/*data fourPatients;*/
/*input ml aa age sbp trt totalcl hdlc dm smk;*/
/*datalines;*/
/*0 0 55 120 0 213 50 0 0*/
/*0 1 55 120 0 213 50 0 0*/
/*1 0 55 120 0 213 50 0 0*/
/*1 1 55 120 0 213 50 0 0*/
/*1 1 85 120 0 213 50 0 0*/
/*;*/
/*run;*/
/*%acc_aha_201310yrCVDrisk( 		DSout=fourPatientsRiskAdded,	*/
/*								DSin=fourPatients,				*/
/*								MALE=ml,						*/
/*								nonHispAA=aa,					*/
/*								AGE=age,						*/
/*								SBP=sbp,						*/
/*								TRTBP=trt,						*/
/*								TCL=totalcl,					*/
/*								HDL=hdlc,						*/
/*								DIAB=dm,						*/
/*								SMOKE=smk						*/
/*							  );				*/






 
	

