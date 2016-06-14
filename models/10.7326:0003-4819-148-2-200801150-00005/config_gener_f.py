# -*- coding: utf-8 -*-

#The purpose of this script is to create a starting place for generating a 
#config file that allows us to reassemble a model and its environment
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

config['model_name'] = 'A Risk Score for Predicting Near-Term Incidence of Hypertension'
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = 'Nonhypertensive Adults ages (20-80)' #NCI Metathesaurus CUI
config['outcome'] = 'C2713447' #unsure of this... #NCI Metathesaurus CUI
config['predictors'] = {}
config['predictors']['function_inputs'] = ["Sex", "Age",  "Systolic BP", "Diastolic BP", "BMI", "Smoking Status", "Parents with Hypertensive History"] #named parameters in the submitted function
config['predictors']['cuis'] = ['C28421','C0804405','C0488055','C0488052','C1542867', 'C3496611','C2713447'] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = ['Male = True','years, 20-80','mm Hg','mm Hg','kg/m^2','y/n','Number of Parents with Hypertensive History'] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = '' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = '1717'
config['model_development_data']['missing_data_strategy'] = ''
config['model_object'] = {}
config['model_object']['file_name'] = '' #name of model object file
config['model_object']['object_name'] = '' #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = 'python' #currently only supports python, R

import json
with open('config_f.json','w') as output:
    json.dump(config,output)



