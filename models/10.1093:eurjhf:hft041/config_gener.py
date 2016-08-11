# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1093/eurjhf:hft041'                # DOI tag                       '99.9999/aaa.a9'
config['id']['papertitle'] = 'Risk Assessment for Incident Heart Failure in Individuals with Atrial Fibrillation'
config['id']['modeltitle'] = 'Simple Multivariable Cox Model (Table 3)'
config['id']['yearofpub'] = '2013'          # year of publication           '2100'
config['id']['authors'] = ['Schnabel, R.B.', 'Rienstra, Michiel']      

# population constraints
config['population'] = {}
config['population']['must'] = ['Atrial Fibrillation']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['Heart Failure']      # unacceptable attributes   ['Doctor of Medicine']
config['population']['mustCUI'] = ['C0004238']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C0018802']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Age','Body Mass Index','Left Ventricular Hypertrophy','Diabetes','Valvular Heart Disease','Myocardial Infarction']
config['input']['description'] = ['Age','Body Mass Index','Left Ventricular Hypertrophy','Diabetes','Significant Murmur','Prevalent Myocardial Infarction']
config['input']['CUI'] = ['C0804405','C1542867','C3484363','C1315719','C1963123','C2926063']
config['input']['units'] = ['years','km/m^2','','','','']
config['input']['datatype'] = ['float','float','bool','bool','bool','bool'] 
config['input']['upper'] = ['','','','','','']
config['input']['lower'] = ['','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '10Y Risk of Heart Failure'               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Heart Failure '         # CVD                      'CVD
config['output']['outcomeTime'] = '10'         # in years                 '10'
config['output']['CUI'] = ''                # kind of risk CUI          'C3176370'
config['output']['outcomeCUI'] = 'C0018802'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['725']      # values for important data         ['8,000,000,000']

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
