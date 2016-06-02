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

config['model_name'] = ''
config['model_category'] = [] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = '' #NCI Metathesaurus CUI
config['outcome'] = '' #NCI Metathesaurus CUI
config['predictors'] = {}
config['predictors']['function_inputs'] = [] #named parameters in the submitted function
config['predictors']['cuis'] = [] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = [] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = '' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = ''
config['model_development_data']['missing_data_strategy'] = ''
config['model_object'] = {}
config['model_object']['file_name'] = '' #name of model object file
config['model_object']['object_name'] = '' #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = '' #currently only supports python, R

import json
with open('config.json','w') as output:
    json.dump(config,output)



