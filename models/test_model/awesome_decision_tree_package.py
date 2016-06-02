# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:37:26 2016

@author: nn31
"""

import pickle
import numpy as np

#maybe would want to a prioir set these named parameters to mean, since that is the imputation
#strategy chosen:
def score_that_data(Fare=7.25,
                    Pclass=3,
                    Sex=0,
                    Age=35,
                    SibSp=0):
    #first let's transform incoming data to something our model expects
    X = np.zeros((2,5))
    X[0] = np.array([Fare,Pclass,Sex,Age,SibSp])       
    clf = pickle.load(open('/Users/nn31/Dropbox/40-githubRrepos/dori/models/test_model/clf.p','rb'))   
    result = clf.predict(X[0:1])
    return(result)
    
    