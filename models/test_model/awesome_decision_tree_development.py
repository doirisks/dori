# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:09:23 2016

@author: nn31
"""
#This is what a researcher's program might look like...

# First they would import the necessary modules and libraries
import pandas as pd
import pickle
train_df = pd.read_csv("/Users/nn31/Dropbox/40-githubRrepos/dori/models/test_model/titanic_train.csv")

#do some preprocessing of the data
train_df["Sex"] = train_df["Sex"].apply(lambda sex: 0 if sex == 'male' else 1)
y = targets = labels = train_df["Survived"].values
columns = ["Fare", "Pclass", "Sex", "Age", "SibSp"]
features = train_df[list(columns)].values

#impute the missing data, note my final model WILL be different if i choose alternate methodology here
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(features)

#fit our model
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X, y)

pickle.dump(clf,open('/Users/nn31/Dropbox/40-githubRrepos/dori/models/test_model/clf.p','wb'))
#now clf is the thing that we're after; however, in order to make 
#it useful, we need to create a function whose inputs are then transformed according 
#to the methodology used in the development process

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
    result = clf.predict(X[0:1])
    return(result)
    

pickle.dump(score_that_data,open('/Users/nn31/Dropbox/40-githubRrepos/dori/models/test_model/clf_func.p','wb'))  