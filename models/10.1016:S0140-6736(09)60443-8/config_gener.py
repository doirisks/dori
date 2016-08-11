# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1016/S0140-6736(09)60443-8'
config['id']['papertitle'] = 'Development of a Risk Score for Atrial Fibrillation in the Community'
config['id']['modeltitle'] = 'Model Available on FHS Website - betas not in paper'
config['id']['yearofpub'] = '2010'
config['id']['authors'] = ['Schnabel, R.B.', 'Sullivan, L.M.'] 

# population constraints
config['population'] = {}
config['population']['must'] = ['']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['Atrial Fibrillation']      # unacceptable attributes   ['Doctor of Medicine']
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C0004238']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Male Sex','Age','Body Mass Index','SBP','Antihypertensive Medication Use','Pr Interval','Significant Murmur','Heart Failure']
config['input']['description'] = ['Male = True','Age','Body Mass Index','Systolic Blood Pressure','Antihypertensive Medication Use','Pr Interval (Seconds)','Valvular Heart Disease','Prevalent Heart Failure']
config['input']['CUI'] = ['C0086582','C0804405','C1542867','C0488055','C0684167','C0488345','C1963123','C0018801']
config['input']['units'] = ['m=T)','years','kg/m^2','mmHg','','seconds','','']
config['input']['datatype'] = ['bool','float','float','float','bool','float','bool','bool']
config['input']['upper'] = ['','','','','','','','']
config['input']['lower'] = ['','','','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '10Y Atrial Fibrillation Risk'               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Atrial Fibrillation'         # CVD                      'CVD
config['output']['outcomeTime'] = '10'         # in years                 '10'
config['output']['CUI'] = 'C3176364' 
config['output']['outcomeCUI'] = 'C0004238'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['4764']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'      # function's language    'python'
config['model']['uncompiled'] = ['model.py']  # some kind of pointer?  ['model.py']
config['model']['compiled'] = ['']    # some kind of pointer?  ['']
config['model']['dependList'] = 'requirements.txt'    # some kind of pointer?  'requirements.txt'
config['model']['example'] = ['example.py']     # some kind of pointer?  ['example.py']

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

config_name = 'config'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config']
