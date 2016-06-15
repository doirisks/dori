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

config['model_name'] = 'Prediction of Incident Diabetes Mellitus in Middle Aged Adults'
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = 'Non-Diabetic Adults, C0205847' #NCI Metathesaurus CUI
config['outcome'] = 'C1716742' #NCI Metathesaurus CUI
config['predictors'] = {}
config['predictors']['function_inputs'] = ["Sex", "Age",  "Systolic BP", "Diastolic BP", "BMI", "HDL-C", "Triglycerides",  "Fasting Glucose", "Parental History of DM", "Antihypertensive Medication Use"] #named parameters in the submitted function
config['predictors']['cuis'] = ['C28421','C0488055','C0488052','C1542867','C0364221','C0364714', 'C0363687', 'C1313937','C0684167'] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = ['Male = True','years','mm Hg','mm Hg','kg/m^2','mg/dL','mg/dL','mg/dL','y/n','y/n'] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = '' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = '3140'
config['model_development_data']['missing_data_strategy'] = ''
config['model_object'] = {}
config['model_object']['file_name'] = '' #name of model object file
config['model_object']['object_name'] = '' #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = 'python' #currently only supports python, R

import json
with open('config_b.json','w') as output:
    json.dump(config,output)



