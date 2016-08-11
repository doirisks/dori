# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/01.CIR.96.1.44'                # DOI tag                       '99.9999/aaa.a9'
config['id']['papertitle'] = 'Intermittent Claudication: A Risk Profile From The Framingham Heart Study' 
config['id']['modeltitle'] = 'Logistic Model'   
config['id']['yearofpub'] = '1997'    
config['id']['authors'] = ['Murabito, J.M.','DAgostino, R.B.']    

# population constraints
config['population'] = {}
config['population']['must'] = ['']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['Intermittent Claudication']
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C0021775']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Sex','Age','Systolic BP','Diastolic BP','Cigarettes per day','Total Cholesterol','Diabetes','Previous CHD']
config['input']['description'] = ['Male = True','Age','Systolic BP','Diastolic BP','Average Cigarettes per day','Total Cholesterol','Diabetes','Previous Coronary Heart Disease']
config['input']['CUI'] = ['C0086582','C0804405','C0488055','C0488052','C3169451','C0364708','C1315719','C2926063']
config['input']['units'] = ['m=T','years','mmHg','mmHg','n/day','mg/dL','','']   
config['input']['datatype'] = ['bool','float','float','float','float','float','bool','bool']
config['input']['upper'] = ['','84','','','','','','']   
config['input']['lower'] = ['','45','','','','','','']   

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '4Y Risk of Intermittent Claudication'
config['output']['outcomeName'] = 'Intermittent Claudication' 
config['output']['outcomeTime'] = '4' 
config['output']['CUI'] = 'C3176361'         
config['output']['outcomeCUI'] = 'C0021775'  

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']  
config['data']['fileurl'] = ['']   
config['data']['datumname'] = ['Sample Size'] 
config['data']['datum'] = ['5209']     

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

print config['config'],
