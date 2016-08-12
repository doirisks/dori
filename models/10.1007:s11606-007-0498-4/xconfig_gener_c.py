# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1007/s11606-007-0498-4'
config['id']['papertitle'] = 'Prediction of One-Year Survival in High-Risk Patients with Acute Coronary Syndromes: Results from the SYNERGY Trial'
config['id']['modeltitle'] = '1 Year Mortality Risk after 30 Days - Table 5'
config['id']['yearofpub'] = '2008'
config['id']['authors'] = ["Mahaffey, Kenneth W.", "Yang, Qinghong ", "Pieper, Karen S. ", "Antman, Elliott M.", "White, Harvey D.", "Goodman, Shaun G.", "Cohen, Marc", "Kleiman, Neal S.", "Langer, Anatoly", "Aylward, Philip E.", "Col, Jacques J.", "Reist, Craig ", "Ferguson, James J.", "Califf, Robert M."]

# population constraints
config['population'] = {}
config['population']['must'] = ['Acute Coronary Syndrome']  # TODO Synergy had fairly complex selection criteria.
                                                            # Inclusion Criteria are all risk factors - unnecessary?
                                                            # No code for "at least two out of 3"
config['population']['mustnot'] = ['known or suspected pregnancy', 'elevated international normalized ratio (>1.5)', 'past or present bleeding disorder'] 
# dis-qualification criteria which could not be "CUIed":
    #'recent (<48 hours) or planned spinal or epidural anesthesia or puncture', 
    #'PCI or thrombolytic therapy within the preceding 24 hours', 
    #'contraindications to unfractionated heparin or LMWH', 
    #'increased risk for bleeding complications due to recent stroke or surgery', 
    #'creatinine clearance less than 30 mL/min',  
config['population']['mustCUI'] = ['C0948089'] 
config['population']['mustnotCUI'] = ['C0032961 or C0425965', 'C0853225', 'C1458140']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = [
    'Male Sex',
    'Age',
    'Heart Rate', 
    'Weight at Baseline',
    'Creatin Clearance',
    'Baseline Platelet',
    'Nadir Platelet',  # relates to other platelets how?
    'Hemoglobin',
    
    'Current Smoker',
    'Former Smoker',
    'Atrial Fibrillation',
    'Prior Coronary Artery Bypass Grafting',
    'History of Diabetes',
    'History of Angina',
    'History of Congestive Heart Failure',
    'ST Depression on Baseline ECG',
    'Baseline Rales',
    'Diagnostic Catheterization',
    
    'Weight after 30 Days',
    'Coronary Artery Bypass Grafting within 30 days',
    'Use of Statin at 30 Days',
    'Percutaneous Coronary Intervention within 30 Days',
    'Use of beta-blockers at 30 days'
]
config['input']['description'] = ['Male Sex', 'Age', 'Heart Rate', 'Weight at Baseline', 'Creatin Clearance', 'Used for Baseline Platelet beyond 200', 'Used for Nadir Platelet up to 200', 'Hemoglobin', 'Current Smoker', 'Former Smoker', 'Atrial Fibrillation', 'Prior Coronary Artery Bypass Grafting', 'History of Diabetes', 'History of Angina', 'History of Congestive Heart Failure', 'ST Depression on Baseline ECG', 'Baseline Rales', 'Diagnostic Catheterization', 'Weight after 30 Days', 'Coronary Artery Bypass Grafting within 30 days', 'Use of Statin at 30 Days', 'Percutaneous Coronary Intervention within 30 Days', 'Use of beta-blockers at 30 days']
config['input']['CUI'] = [
    'C0086582',
    'C0804405',
    'C0488794',
    'C0043100',
    'C1507751',
    'C0942474',
    'NOCUINADIRPLATELETS',
    'C0482781',
    
    'C3173209',
    'C0337671',
    'C0004238',
    'C1275842',
    'C1315719',
    'C0002962',
    'C0018802',
    'C0520887',
    'C0034642',
    'C0596429',
    
    'C0043100AT30DAYS',
    'C1275842AT30DAYS',
    'C2585159AT30DAYS',
    'C1532338AT30DAYS',
    'C3710293AT30DAYS'
]
config['input']['units'] = ['', 'years', 'bpm', 'kg', 'mL/min', '10^3/mm^3', '10^3/mm^3', 'g/dL', '', '', '', '', '', '', '', '', '', '', 'kg', '', '', '', '']
config['input']['datatype'] = ['bool', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool', 'bool', 'bool']
config['input']['upper'] = [''] * 23
config['input']['lower'] = ['', '30'] + [''] * 21

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '1Y Risk of Death'
config['output']['outcomeName'] = 'Death'
config['output']['outcomeTime'] = "1"
config['output']['CUI'] = ''
config['output']['outcomeCUI'] = 'CL480147' 

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = [''] 
config['data']['fileurl'] = ['']  
config['data']['datumname'] = ['Sample Size']  
config['data']['datum'] = ['9978'] 

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
