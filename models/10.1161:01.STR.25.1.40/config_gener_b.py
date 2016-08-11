# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/01.STR.25.1.40'  
config['id']['papertitle'] = 'Stroke Risk Profile: Adjustment for Antihypertensive Medication'      
config['id']['modeltitle'] = 'Risk Score by Point System (Tables 2 and 3)'     #TODO
config['id']['yearofpub'] = '1994'          
config['id']['authors'] = ["DAgostino, R.B.","Wolf, P.A.", "Belanger, A.J.","Kannel, W.B."]

# population constraints
config['population'] = {}
config['population']['must'] = ['']
config['population']['mustnot'] = ['Stroke'] 
config['population']['mustCUI'] = ['']     
config['population']['mustnotCUI'] = ['C0038454']   

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["Male Sex", "Age", "Systolic BP", "Antihypertensive Medication Use", "Cardiovascular Disease", "Left Ventricular Hypertrophy", "Cigarettes", "Atrial Fibrillation", "Diabetic"]     
config['input']['description'] = ["Male Sex", "Age", "Systolic BP", "Antihypertensive Medication Use", "Cardiovascular Disease", "Left Ventricular Hypertrophy", "Cigarettes", "Atrial Fibrillation", "Diabetic"]    
config['input']['CUI'] = ["C0086582", "C0804405", "C0488055", "C0684167","C0007222", "C3484363", "C3173717", "C0004238", "C1315719" ]
config['input']['units'] = ["","years","mmHg","","","","","",""] 
config['input']['datatype'] = ["bool","float","float","bool","bool","bool","bool","bool","bool"]   
config['input']['upper'] = ["","85","216","","","","","",""] 
config['input']['lower'] = ["","55", "95","","","","","",""] 

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '10Y Risk of Stroke'
config['output']['outcomeName'] = 'Stroke'
config['output']['outcomeTime'] = '10'
config['output']['CUI'] = 'C3176363'
config['output']['outcomeCUI'] = 'C0038454'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['5734']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'R'
config['model']['uncompiled'] = ['model_b.R']
config['model']['compiled'] = ['model_b.Rdata','model_df_b.Rdata','model_b_table.Rdata']
config['model']['dependList'] = 'requirements.txt'        # requirements.txt?
config['model']['example'] = ['example_b.py']     

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

config_name = 'config_b'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config']
