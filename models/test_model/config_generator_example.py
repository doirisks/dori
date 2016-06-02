# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:16:19 2016

@author: nn31
"""

#The purpose of this script is to create a starting place for generating a 
#config file that allows us to reassemble a model and its environment
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

config['model_name'] = 'My Test Model'
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = 'C0524646' #NCI Metathesaurus CUI
config['outcome'] = 'C0013142' #NCI Metathesaurus CUI
config['predictors'] = {}
config['predictors']['function_inputs'] = ["Fare", "Pclass", "Sex", "Age", "SibSp"] #named parameters in the submitted function
config['predictors']['cuis'] = ["C1555442", "C0456387", "C0015780", "C0001779", "C0162409"] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = ["US dollar amount for ticket", "Passenger Class [1,2,3]", "Female (1,0)", "Age (years)", "Spouse Onboard (1,0)"] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = 'requirements.txt' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = '891'
config['model_development_data']['missing_data_strategy'] = 'mean imputation'
config['model_object'] = {}
config['model_object']['file_name'] = 'awesome_decision_tree_package.py' #name of model object file
config['model_object']['object_name'] = 'score_that_data' #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = 'python' #currently only supports python, R

import os
os.chdir('/Users/nn31/Dropbox/40-githubRrepos/dori/models/test_model')

import json
with open('config.json','w') as output:
    json.dump(config,output)



