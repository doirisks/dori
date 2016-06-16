# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.7326/0003-4819-148-2-200801150-00005'
config['id']['papertitle'] = 'A Risk Score for Predicting Near-Term Incidence of Hypertension'
config['id']['modeltitle'] = '1 Year Weibull'  
config['id']['yearofpub'] = '2008' 
config['id']['authors'] = ['Parikh, N.I.','Pencina,M.J.'] 

# population constraints
config['population'] = {}
config['population']['must'] = ['']    
config['population']['mustnot'] = ['Hypertension'] 
config['population']['mustCUI'] = [''] 
config['population']['mustnotCUI'] = ['C1717437'] 

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["Sex", "Age",  "Systolic BP", "Diastolic BP", "BMI", "Smoking Status", "Parental Hypertensive History"]
config['input']['description'] = ["Male = True", "Age",  "Systolic BP", "Diastolic BP", "BMI", "Tobacco Smoking Status", "Number of Parents with Hypertensive History"]
config['input']['CUI'] = ['C28421','C0804405','C0488055','C0488052','C1542867', 'C3496611','C2713447']             # CUIs for each input, IN ORDER                   ['C0804405','C28421']
config['input']['units'] = ["m=T", "years",  "mmHg", "mmHg", "kg/m^2", "", "neither, one, two"]
config['input']['datatype'] = ["bool", "float",  "float", "float", "float", "bool", "int"]
config['input']['upper'] = ['','80','','','','','']
config['input']['lower'] = ['','20','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '1Y Risk of Hypertension'   
config['output']['outcomeName'] = 'Hypertension'       
config['output']['outcomeTime'] = '1'      
config['output']['CUI'] = ''
config['output']['outcomeCUI'] = 'C1717437'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['1717']      # values for important data         ['8,000,000,000']

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
    print modvalues[i]
    modvalues[i] = modvalues[i].replace("'","''")
    print modvalues[i]

print len(modvalues)

insertion = models_table.insert(columns = columns, values = [modvalues])


model_tup = tuple(insertion)
query = model_tup[0].replace('%s',"'%s'").replace('"','')

query = query % tuple(model_tup[1])
print query

#query = format(model_tup[0],*model_tup[1])

sqlfile.write(query)
sqlfile.close()
