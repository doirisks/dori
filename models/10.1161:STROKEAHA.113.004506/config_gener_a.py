# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1161/STROKEAHA.113.004506'
config['id']['papertitle'] = 'Intracranial Hemorrhage Among Patients With Atrial Fibrillation Anticoagulated With Warfarin or Rivaroxaban'
config['id']['modeltitle'] = 'PANWARDS Nomogram Point System (Tables 4 and 5)'
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
config['output']['name'] = '2.5Y Risk of Intracranial Hemorrhage'
config['output']['outcomeName'] = 'Intracranial Hemorrhage'
config['output']['outcomeTime'] = '2.5'
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
# dump sql config file 
import sql
models_table = sql.Table('models')

modvalues = [
    config['id']['DOI'],
    config['id']['papertitle'],
    config['id']['modeltitle'],
    config['id']['yearofpub'],
    json.dumps(config['id']['authors']),
    
    json.dumps(config['population']['must']),
    json.dumps(config['population']['mustnot']),
    json.dumps(config['population']['mustCUI']),
    json.dumps(config['population']['mustnotCUI']),
    
    json.dumps(config['input']['name']),
    json.dumps(config['input']['description']),
    json.dumps(config['input']['CUI']),
    json.dumps(config['input']['units']),
    json.dumps(config['input']['datatype']),
    json.dumps(config['input']['upper']),
    json.dumps(config['input']['lower']),
    
    config['output']['name'],
    config['output']['outcomeName'],
    config['output']['outcomeTime'],
    config['output']['CUI'],
    config['output']['outcomeCUI'],
    
    json.dumps(config['data']['filename']),
    json.dumps(config['data']['fileurl']),
    json.dumps(config['data']['datumname']),
    json.dumps(config['data']['datum']),
    
    config['model']['language'],
    json.dumps(config['model']['uncompiled']),
    json.dumps(config['model']['compiled']),
    config['model']['dependList'],
    json.dumps(config['model']['example']),
    
    json.dumps(config['model_category']),
    json.dumps(config['predictive_ability']['type']),
    json.dumps(config['predictive_ability']['metric']),
    json.dumps(config['predictive_ability']['value']),
    json.dumps(config['predictive_ability']['lcl']),
    json.dumps(config['predictive_ability']['ucl']),

    config['config']
]


columns = [models_table.DOI,models_table.papertitle, models_table.modeltitle, models_table.yearofpub,  models_table.authors, models_table.must, models_table.mustnot,models_table.mustCUI, models_table.mustnotCUI,  models_table.inpname, models_table.inpdesc, models_table.inpCUI,models_table.inpunits,models_table.inpdatatype, models_table.upper, models_table.lower, models_table.output, models_table.outcome,models_table.outcometime, models_table.outputCUI, models_table.outcomeCUI, models_table.filename,models_table.filepointer, models_table.datumname,models_table.datum, models_table.language,models_table.uncompiled,models_table.compiled,models_table.dependList,models_table.example, models_table.model_category,models_table.type,models_table.metric,models_table.value, models_table.lcl, models_table.ucl, models_table.config, models_table.numofinputs]
# numofinputs was added after the fact!

for i in range(len(modvalues)):
    modvalues[i] = modvalues[i].replace("'","''")


insertion = models_table.insert(columns = columns, values = [ modvalues + [len(config['input']['CUI'])] ]) 


model_tup = tuple(insertion)
query = model_tup[0].replace('%s',"'%s'").replace('"','')

query = query % tuple(model_tup[1])

#query = format(model_tup[0],*model_tup[1])

print(query + ';\n')
