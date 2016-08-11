# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/01.CIR.97.18.1837'                # DOI tag                       
config['id']['papertitle'] = 'Prediction of Coronary Heart Disease Using Risk Factor Categories'   
config['id']['modeltitle'] = 'Total Cholesterol Point System (Figures 3 & 4)' 
config['id']['yearofpub'] = '1998'     
config['id']['authors'] = ['Wilson, P.W.', "DAgostino,R.B."]         

# population constraints
config['population'] = {}
config['population']['must'] = ['']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['Coronary Heart Disease']      # unacceptable attributes   ['Doctor of Medicine']
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C2926063']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["sex", "age", "total cholesterol", "hdl cholesterol", "systolic BP", "diastolic BP", "diabetic", "smoker"]            # human readable, e.g.                              ['age','gender']
config['input']['description'] = ["Male = True", "age", "total cholesterol", "hdl cholesterol", "systolic BP", "diastolic BP", "diabetic", "smoker"] 
config['input']['CUI'] = ['C0086582','C0804405','C0364708','C0364221','C0488055','C0488052','C1315719','C3496611']
config['input']['units'] = ["m=T", "years", "mg/dL", "mg/dL", "mmHg", "mmHg", "", ""]
config['input']['datatype'] = ["bool", "float", "float", "float", "float", "float", "bool", "bool"]
config['input']['upper'] = ["", "74", "", "", "", "", "", ""]
config['input']['lower'] = ["", "30", "", "", "", "", "", ""]

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '10Y Risk of Coronary Heart Disease'
config['output']['outcomeName'] = 'Coronary Heart Disease'
config['output']['outcomeTime'] = '10'         # in years 
config['output']['CUI'] = 'C3176182'                # kind of risk CUI          'C3176370'
config['output']['outcomeCUI'] = 'C2926063'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['5345']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'      # function's language    'python'
config['model']['uncompiled'] = ['model_c.py']  # some kind of pointer?  ['model.py']
config['model']['compiled'] = ['']    # some kind of pointer?  ['']
config['model']['dependList'] = 'requirements.txt'    # some kind of pointer?  'requirements.txt'
config['model']['example'] = ['example_c.py']     # some kind of pointer?  ['example.py']

# I do not know what this would be used for
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'

# I do not know what these are for...
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] 
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []

config_name = 'config_c'

config['config'] = config_name + '.json'

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

print config['config'],
