# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1016/S0140-6736(09)60443-8'
config['id']['papertitle'] = 'Development of a Risk Score for Atrial Fibrillation in the Community'
config['id']['modeltitle'] = 'Model Available on FHS Website - betas not in paper'
config['id']['yearofpub'] = '2010'
config['id']['authors'] = ['Schnabel, R.B.', 'Sullivan, L.M.'] 

# population constraints
config['population'] = {}
config['population']['must'] = ['']         # necessary attributes      ['Pedal Cyclist']
config['population']['mustnot'] = ['Atrial Fibrillation']      # unacceptable attributes   ['Doctor of Medicine']
config['population']['mustCUI'] = ['']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['C0004238']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ['Male Sex','Age','Body Mass Index','SBP','Antihypertensive Medication Use','Pr Interval','Significant Murmur','Heart Failure']
config['input']['description'] = ['Male = True','Age','Body Mass Index','Systolic Blood Pressure','Antihypertensive Medication Use','Pr Interval (Seconds)','Valvular Heart Disease','Prevalent Heart Failure']
config['input']['CUI'] = ['C28421','C0804405','C1542867','C0488055','C0684167','C0488345','C1963123','C0018801']
config['input']['units'] = ['m=T)','years','kg/m^2','mmHg','','seconds','','']
config['input']['datatype'] = ['bool','float','float','float','bool','float','bool','bool']
config['input']['upper'] = ['','','','','','','','']
config['input']['lower'] = ['','','','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '10Y Atrial Fibrillation Risk'               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Atrial Fibrillation'         # CVD                      'CVD
config['output']['outcomeTime'] = '10'         # in years                 '10'
config['output']['CUI'] = 'C3176364' 
config['output']['outcomeCUI'] = 'C0004238'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['4764']      # values for important data         ['8,000,000,000']

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
