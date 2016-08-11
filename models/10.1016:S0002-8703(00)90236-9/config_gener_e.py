# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1016/S0002-8703(00)90236-9' 
config['id']['papertitle'] = 'Primary and subsequent coronary risk appraisal: New results from The Framingham Study'
config['id']['modeltitle'] = 'Subsequent CHD, Weibull 2 years'
config['id']['yearofpub'] = '2000'          # year of publication           '2100'
config['id']['authors'] = ["D'Agostino, R.B.","Russell, M.W."]

# population constraints
config['population'] = {}
config['population']['must'] = ['Coronary Heart Disease']   
config['population']['mustnot'] = ['']
config['population']['mustCUI'] = ['C0018802']
config['population']['mustnotCUI'] = [''] 

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["sex","age","total cholesterol","hdl cholesterol","systolic BP", "diabetes", "Cigarette Smoking"]
config['input']['description'] = ["sex","age","total cholesterol","hdl cholesterol","systolic BP", "diabetes", "Cigarette Smoking"]
config['input']['CUI'] = ['C0086582','C0804405','C0364708','C0364221','C0488055','C1315719', 'C3173717']   
config['input']['units'] = ['male=T','years','mg/dL','mg/dL','mmHg','',''] 
config['input']['datatype'] = ['bool','float','float','float','float','bool','bool']    
config['input']['upper'] = ['','74','','','','',''] 
config['input']['lower'] = ['','35','','','','','']   

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = ''               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Coronary Heart Disease'         # CVD                      'CVD
config['output']['outcomeTime'] = '2'         # in years                 '10'
config['output']['CUI'] = ''                # kind of risk CUI          'C3176370'
config['output']['outcomeCUI'] = 'C0018802'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['1176']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'      # function's language    'python'
config['model']['uncompiled'] = ['model_e.py']  # some kind of pointer?  ['model.py']
config['model']['compiled'] = ['']    # some kind of pointer?  ['']
config['model']['dependList'] = 'requirements.txt'    # some kind of pointer?  'requirements.txt'
config['model']['example'] = ['example_e.py']     # some kind of pointer?  ['example.py']

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

config_name = 'config_e'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config']
