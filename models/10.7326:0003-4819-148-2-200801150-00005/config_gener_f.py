# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.7326/0003-4819-148-2-200801150-00005'
config['id']['papertitle'] = 'A Risk Score for Predicting Near-Term Incidence of Hypertension'
config['id']['modeltitle'] = '4 Point System'  
config['id']['yearofpub'] = '2008' 
config['id']['authors'] = ['Parikh, N.I.','Pencina,M.J.'] 

# population constraints
config['population'] = {}
config['population']['must'] = ['']    
config['population']['mustnot'] = ['Hypertension'] 
config['population']['mustCUI'] = [''] 
config['population']['mustnotCUI'] = ['C1717437'] 

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["Sex", "Age",  "Systolic BP", "Diastolic BP", "BMI", "Smoking Status", "Parental Hypertensive History"]
config['input']['description'] = ["Male = True", "Age",  "Systolic BP", "Diastolic BP", "BMI", "Tobacco Smoking Status", "Number of Parents with Hypertensive History"]
config['input']['CUI'] = ['C0086582','C0804405','C0488055','C0488052','C1542867', 'C3496611','C2713447']             # CUIs for each input, IN ORDER                   ['C0804405','C28421']
config['input']['units'] = ["m=T", "years",  "mmHg", "mmHg", "kg/m^2", "", "neither, one, two"]
config['input']['datatype'] = ["bool", "float",  "float", "float", "float", "bool", "int"]
config['input']['upper'] = ['','80','','','','','']
config['input']['lower'] = ['','20','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '4Y Risk of Hypertension'   
config['output']['outcomeName'] = 'Hypertension'       
config['output']['outcomeTime'] = '4'
config['output']['CUI'] = ''
config['output']['outcomeCUI'] = 'C1717437'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['1717']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'      # function's language    'python'
config['model']['uncompiled'] = ['model_f.py']  # some kind of pointer?  ['model.py']
config['model']['compiled'] = ['']    # some kind of pointer?  ['']
config['model']['dependList'] = 'requirements.txt'    # some kind of pointer?  'requirements.txt'
config['model']['example'] = ['example_f.py']     # some kind of pointer?  ['example.py']

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

config_name = 'config_f'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config']
