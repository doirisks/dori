# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1001/archinte.167.10.1068'                # DOI tag                       '99.9999/aaa.a9'
config['id']['papertitle'] = 'Prediction of Incident Diabetes Mellitus in Middle Aged Adults'
config['id']['modeltitle'] = 'Point System'         # name of specific model        'Demo Model'
config['id']['yearofpub'] = '2007'          # year of publication           '2100'
config['id']['authors'] = ['Wilson, W.F.'] 

# population constraints
config['population'] = {}
config['population']['must'] = ['']
config['population']['mustnot'] = ['Type 2 Diabetes Mellitus']      
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C1832387']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["Sex", "Age",  "Systolic BP", "Diastolic BP", "BMI", "HDL-C", "Triglycerides",  "Fasting Glucose", "Parental History of DM", "Antihypertensive Medication Use"]     
config['input']['description'] = [] 
config['input']['CUI'] = ['C28421','C0804405','C0488055','C0488052','C1542867','C0364221', 'C0364714', 'C0363687', 'C1313937','C0684167']      
config['input']['units'] = ['m=T','years','mmHg','mmHg','kg/m^2','mg/dL','mg/dL','mg/dL','','']
config['input']['datatype'] = ['bool','float','float','float','float','float','float','float','int','bool'] 
config['input']['upper'] = ['','','','','','','','126','2','']
config['input']['lower'] = ['','','','','','','','','0','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = ''               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Type 2 Diabetes Mellitus'         # CVD                      'CVD
config['output']['outcomeTime'] = '8'         # in years                 '10'
config['output']['CUI'] = ''                # kind of risk CUI          'C3176370'
config['output']['outcomeCUI'] = 'C1832387'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['3140']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'      # function's language    'python'
config['model']['uncompiled'] = ['model_a.py']  # some kind of pointer?  ['model.py']
config['model']['compiled'] = ['']    # some kind of pointer?  ['']
config['model']['dependList'] = 'requirements.txt'    # some kind of pointer?  'requirements.txt'
config['model']['example'] = ['example_a.py']     # some kind of pointer?  ['example.py']

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

import json
with open('config_a.json','w') as output:
    json.dump(config,output)
