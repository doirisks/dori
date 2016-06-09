#The purpose of this script is to create a starting place for generating a 
#config file that allows us to reassemble a model and its environment
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

config['model_name'] = 'Primary and subsequent coronary risk appraisal: New results from The Framingham Study'
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = 'C3166034' #NCI Metathesaurus CUI
config['outcome'] = 'C3176373' #NCI Metathesaurus CUI
config['predictors'] = {}
config['predictors']['function_inputs'] = ["sex","age","total cholesterol","hdl cholesterol","systolic BP", "diabetes", "Cigarette Smoking"] #named parameters in the submitted function
config['predictors']['cuis'] = ['C28421','C0804405','C0364708','C0364221','C0488055','C1315719', 'C3173717'] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = ['male=T','years','mg/dL','mg/dL','mmHg','',''] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = '' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = '1176'
config['model_development_data']['missing_data_strategy'] = ''
config['model_object'] = {}
config['model_object']['file_name'] = '' #name of model object file
config['model_object']['object_name'] = '' #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = 'python' #currently only supports python, R

import json
with open('config_e.json','w') as output:
    json.dump(config,output)
