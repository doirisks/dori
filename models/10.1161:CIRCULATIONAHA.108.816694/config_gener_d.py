# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/CIRCULATIONAHA.108.816694'
config['id']['papertitle'] = 'Predicting the Thirty-year Risk of Cardiovascular Disease'
config['id']['modeltitle'] = 'Hard CVD, cholesterol'         # name of specific model        'Demo Model'
config['id']['yearofpub'] = '2009'          # year of publication           '2100'
config['id']['authors'] = ['Pencina, M.J.','DAgostino, R.B.']  


# population constraints
config['population'] = {}
config['population']['must'] = ['']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['Cardiovascular Disease','Cancer']
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C0007222','C2707253']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Sex','Age','SBP','Antihypertensive Medication Use','Smoking','Diabetes', 'BMI']
config['input']['description'] = ['Male = True','Age','Systolic Blood Pressure','Antihypertensive Medication Use','Smoking','Diabetes','BMI']
config['input']['CUI'] = ['C0086582','C0804405','C0488055','C0684167','C3496611','C1315719', 'C1542867']
config['input']['units'] = ['m=T','years','mmHg','','','','kg/m^2']
config['input']['datatype'] = ['bool','float','float','bool','bool','bool','float']
config['input']['upper'] = ['','59','','','','','']
config['input']['lower'] = ['','20','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '30Y Hard Cardiovascular Risk'               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Hard CVD (coronary death, myocardial infarction, stroke)'
config['output']['outcomeTime'] = '30'         # in years                 '10'
config['output']['CUI'] = ''                # kind of risk CUI          'C3176370'
config['output']['outcomeCUI'] = 'C2926092 or C2926063 or C0038454'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['4506']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'
config['model']['uncompiled'] = ['modeld.py'] 
config['model']['compiled'] = ['']    
config['model']['dependList'] = 'requirements.txt' 
config['model']['example'] = ['exampled.py']    

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

config_name = 'config_d'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config']
