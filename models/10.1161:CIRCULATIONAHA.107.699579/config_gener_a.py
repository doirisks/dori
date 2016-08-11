# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/CIRCULATIONAHA.107.699579'
config['id']['papertitle'] = 'General Cardiovascular Risk Profile for Use in Primary Care'
config['id']['modeltitle'] = 'Cox Regression Model'         
config['id']['yearofpub'] = '2008'          # year of publication           '2100'
config['id']['authors'] = ['DAgostino, R.B.','Vasan, R.S.','Pencina, M.J.', 'Wolf, Philip A.', 'Cobain, Mark', 'Massaro, Joseph M.', 'Kannel, William B.']


# population constraints
config['population'] = {}
config['population']['must'] = ['']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['General Cardiovascular Disease']      # unacceptable attributes   ['Doctor of Medicine']
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C0007222']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Sex','Antihypertensive Medication Use','Age','Total Cholesterol','Hdl Cholesterol','Sbd','Smoking','Diabetes']
config['input']['description'] = ['Sex (Male = True)','Antihypertensive Medication Use','Age','Total Cholesterol','Hdl Cholesterol','Systolic Blood Pressure','Smoking','Diabetes']  
config['input']['CUI'] = ['C0086582','C0684167','C0804405','C0364708','C0364221','C0488055','C3496611','C1315719']
config['input']['units'] = ['','','years','mg/dL','mg/dL','mmHg','','']   
config['input']['datatype'] = ['bool','bool','float','float','float','float','bool','bool']
config['input']['upper'] = ['','','74','','','','','']
config['input']['lower'] = ['','','30','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '10Y General Cardiovascular Disease Risk'   
config['output']['outcomeName'] = 'General Cardiovascular Disease' 
config['output']['outcomeTime'] = '10'  
config['output']['CUI'] = 'C3176186'    
config['output']['outcomeCUI'] = 'C0007222'  

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Male Sample Size', 'Female Sample Size']  # important data for easy access    ['Male Sample Size', 'Female Sample Size']
config['data']['datum'] = ['3969', '4522']      # values for important data         ['8,000,000,000']

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

config_name = 'config_a'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config']
