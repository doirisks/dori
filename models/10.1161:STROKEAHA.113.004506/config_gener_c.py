# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/STROKEAHA.113.004506'
config['id']['papertitle'] = 'Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban'
config['id']['modeltitle'] = 'Cox Model for Intracranial Hemorrhage'
config['id']['yearofpub'] = '2014'
config['id']['authors'] = ["Hankey, Graeme J.", "Stevens, Susanna R.", "Piccini, Jonathan P.", "Lokhnygina, Yuliya", "Mahaffey, Kenneth W.", "Halperin, Jonathan L.", "Patel, Manesh R.", "Breithardt, Gunter", "Singer, Daniel E.", "Becker, Richard C.", "Berkowitz, Scott D.", "Paolini, John F.", "Nessel, Christopher C.", "Hacke, Werner", "Fox, Keith A.A.", "Califf, Robert M."]

# population constraints
config['population'] = {}
config['population']['must'] = ['Warfarin or Rivaroxaban']
config['population']['mustnot'] = [''] 
config['population']['mustCUI'] = ['C1532949 or C1739768'] 
config['population']['mustnotCUI'] = [''] 

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Age', 'Diastolic Blood Pressure', 'Platelets','Albumin','History of Coronary Heart Failure', 'History of Stroke or TIA', 'Asian Ethnicity', 'Black Ethnicity', 'Warfarin', 'Rivaroxaban']
config['input']['description'] = ['Age', 'Diastolic Blood Pressure', 'Platelets','Albumin','History of Coronary Heart Failure', 'History of Stroke or TIA', 'Asian Ethnicity', 'Black Ethnicity', 'Warfarin', 'Rivaroxaban']
config['input']['CUI'] = ['C0804405', 'C0488052', 'C1977245', 'C0363892', 'C0018802', 'C0038454 or C0007787', 'C0078988', 'C0005680', 'C1532949', 'C1739768']
config['input']['units'] = ['years', 'mmHg', '10^9/L', 'g/dL',  '', '', '', '', '', '']
config['input']['datatype'] = ['float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'] 
config['input']['upper'] = ['', '', '', '', '', '', '', '', '', '']
config['input']['lower'] = ['18', '', '', '', '', '', '', '', '', '']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = str(1036.6944444445 / 365.25) + 'Y Risk of Intracranial Hemorrhage'
config['output']['outcomeName'] = 'Intracranial Hemorrhage'
config['output']['outcomeTime'] = str(1036.6944444445 / 365.25)
config['output']['CUI'] = ''
config['output']['outcomeCUI'] = 'C0151699' 

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = [''] 
config['data']['fileurl'] = ['']  
config['data']['datumname'] = ['Sample Size']  
config['data']['datum'] = ['13739'] 

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

print config['config']
