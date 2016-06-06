#The purpose of this script is to create a starting place for generating a 
#config file that allows us to reassemble a model and its environment
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

config['model_name'] = 'Predicting the Thirty-year Risk of Cardiovascular Disease'
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = 'C0001675' #NCI Metathesaurus CUI
config['outcome'] = '30yr Risk (no CUI)' #NCI Metathesaurus CUI 
config['predictors'] = {}
config['predictors']['function_inputs'] = ['Sex (Male = True)','Age','Sbd (Systolic Blood Pressure)','Antihypertensive Medication Use','Smoking','Diabetes','Total Cholesterol','Hdl Cholesterol','Body Mass Index'] #named parameters in the submitted function
config['predictors']['cuis'] = ['C28421','C0804405','C0488055','C0684167','C3496611','C1315719','C0364708','C0364221','C1542867'] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = ['Categorical','Quantitative','Quantitative','Categorical', 'Categorical','Categorical','Quantitative','Quantitative','Quantitative'] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = '' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = '2333 male, 2173 female'
config['model_development_data']['missing_data_strategy'] = ''
config['model_object'] = {}
config['model_object']['file_name'] = None #name of model object file
config['model_object']['object_name'] = None #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = 'python' #currently only supports python, R

import json
with open('config.json','w') as output:
    json.dump(config,output)
