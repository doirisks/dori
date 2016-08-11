# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1001/jama.290.8.1093'
config['id']['papertitle'] = 'A Risk Score for Predicting Stroke or Death in Individuals With New-Onset Atrial Fibrillation in the Community'
config['id']['modeltitle'] = 'Cox Regression Model, Warfarin Censored (Stroke or Death)'
config['id']['yearofpub'] = '2003'          # year of publication           '2100'
config['id']['authors'] = ['Wang, T.J.','Massaro,J.M.','Levy, D.', 'Vasan, R.S.', 'Wolf, P.A.', "DAgostino, R.B.", 'Larson, M.G.', 'Kannel, W.B.', 'Benjamin, E.J.']


# population constraints
config['population'] = {}
config['population']['must'] = ['']#['New-Onset Atrial Fibrillation'] 
config['population']['mustnot'] = ['Treated with Warfarin'] #['Prior Atrial Fibrillation', 'Treated with Warfarin']
config['population']['mustCUI'] = [''] #['NOCUI']      #C0004238 "new-onset" is NOT accounted for.
config['population']['mustnotCUI'] = ['C1532949'] #['NOCUI', 'C1532949']   #C0004238 "prior" is NOT accounted for.

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Age', 'Systolic Blood Pressure', 'Diabetes Mellitus', 'Prior CHF or MI', 'Cigarettes in Previous Year', 'Valvular Heart Disease', 'ECG Left Ventricular Hypertrophy']
config['input']['description'] = ['Age', 'Systolic Blood Pressure', 'Diabetes Mellitus', 'Prior Congestive Heart Failure or Heart Attack', 'Cigarettes in Previous Year', 'Significant Murmur', 'ECG Left Ventricular Hypertrophy']  
config['input']['CUI'] = ['C0804405','C0488055','C1716742','C0018801 or C2926063','C0700219','C1963123','C3484363']
config['input']['units'] = ['years','mmHg','','','','','']   
config['input']['datatype'] = ['float','float','bool','bool','bool','bool','bool']
config['input']['upper'] = ['94','','','','','','']
config['input']['lower'] = ['55','','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '5Y Stroke or Death Risk after Atrial Fibrillation'   
config['output']['outcomeName'] = 'Stroke or Death' 
config['output']['outcomeTime'] = '5'  
config['output']['CUI'] = 'C3166384'    
config['output']['outcomeCUI'] = 'C0038454 or CL480147'  

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['705']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'R'      # function's language    'python'
config['model']['uncompiled'] = ['model_b.R']  # some kind of pointer?  ['model.py']
config['model']['compiled'] = ['model_b.Rdata','model_df_b.Rdata']    # some kind of pointer?  ['']
config['model']['dependList'] = 'requirements.txt'    # some kind of pointer?  'requirements.txt'
config['model']['example'] = ['example_b.R']     # some kind of pointer?  ['example.py']

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
