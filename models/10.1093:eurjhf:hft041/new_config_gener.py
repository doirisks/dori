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
config['input']['units'] = ['Age','Body Mass Index','Left Ventricular Hypertrophy','Diabetes','Valvular Heart Disease (Significant Murmur)','Prevalent Myocardial Infarction']
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

# dump json config file
import json
with open(config_name + '.json','w') as output:
    json.dump(config,output)

# dump sql config file 
import sql
sqlfile = open(config_name + '.sql','w')
models_table = sql.Table('models')

modvalues = [
    config['id']['DOI'],
    config['id']['papertitle'],
    config['id']['modeltitle'],
    config['id']['yearofpub'],
    str(config['id']['authors']),
    
    str(config['population']['must']),
    str(config['population']['mustnot']),
    str(config['population']['mustCUI']),
    str(config['population']['mustnotCUI']),
    
    str(config['input']['name']),
    str(config['input']['description']),
    str(config['input']['CUI']),
    str(config['input']['units']),
    str(config['input']['datatype']),
    str(config['input']['upper']),
    str(config['input']['lower']),
    
    config['output']['name'],
    config['output']['outcomeName'],
    config['output']['outcomeTime'],
    config['output']['CUI'],
    config['output']['outcomeCUI'],
    
    str(config['data']['filename']),
    str(config['data']['fileurl']),
    str(config['data']['datumname']),
    str(config['data']['datum']),
    
    config['model']['language'],
    str(config['model']['uncompiled']),
    str(config['model']['compiled']),
    config['model']['dependList'],
    str(config['model']['example']),
    
    str(config['model_category']),
    str(config['predictive_ability']['type']),
    str(config['predictive_ability']['metric']),
    str(config['predictive_ability']['value']),
    str(config['predictive_ability']['lcl']),
    str(config['predictive_ability']['ucl'])
]


columns = [models_table.DOI,models_table.papertitle, models_table.modeltitle, models_table.yearofpub,  models_table.authors, models_table.must, models_table.mustnot,models_table.mustCUI, models_table.mustnotCUI,  models_table.inpname, models_table.inpdesc, models_table.inpCUI,models_table.inpunits,models_table.inpdatatype, models_table.upper, models_table.lower, models_table.output, models_table.outcome,models_table.outcometime, models_table.outputCUI, models_table.outcomeCUI, models_table.filename,models_table.filepointer, models_table.datumname,models_table.datum, models_table.language,models_table.uncompiled,models_table.compiled,models_table.dependList,models_table.example, models_table.model_category,models_table.type,models_table.metric,models_table.value, models_table.lcl, models_table.ucl]


for i in range(len(modvalues)):
    modvalues[i] = modvalues[i].replace("'","''")

insertion = models_table.insert(columns = columns, values = [modvalues])


model_tup = tuple(insertion)
query = model_tup[0].replace('%s',"'%s'").replace('"','')

query = query % tuple(model_tup[1])

#query = format(model_tup[0],*model_tup[1])

sqlfile.write(query)
sqlfile.close()
