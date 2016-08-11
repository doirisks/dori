# -*- coding: utf-8 -*-

# a template for making config.json files for functions
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

# human and machine readable names for the model
config['id'] = {}
config['id']['DOI'] = '10.1001/archinte.159.11.1197'    
config['id']['papertitle'] = 'Profile for Estimating Risk of Heart Failure'        
config['id']['modeltitle'] = '4Y Heart Failure Risk, Simple Score'   
config['id']['yearofpub'] = '1999'      
config['id']['authors'] = ['William, B. Kannel']

# population constraints
config['population'] = {}
config['population']['must'] = ['Coronary Attacks, Valvular Heart Disease, or Hypertension']   
config['population']['mustnot'] = ['']      # unacceptable attributes   ['Doctor of Medicine']
config['population']['mustCUI'] = ['C2926063 or C1963123 or C1717437']      # CUIs for necessary        ['C0810085']
config['population']['mustnotCUI'] = ['']   # CUIs for unacceptable     ['C1512018']

# human and machine readable input descriptions
config['input'] = {}
config['input']['name'] = ["sex", "age", "LVH", "heart rate", "systolic bp", "Coronary Heart Disease", "valve disease", "diabetes", "BMI"]
config['input']['description'] = ['','','Left Ventricular Hypertrophy','','','Myocardial Infarction','Significant Murmur','','Body Mass Index']
config['input']['CUI'] = ['C0086582','C0804405','C3484363','C0488794','C0488055', 'C2926063', 'C1963123', 'C1315719','C1542867']             # CUIs for each input, IN ORDER                   ['C0804405','C28421']
config['input']['units'] = ['m=T','years','','bpm','mmHg','','','','kg/m^2']        
config['input']['datatype'] = ['bool','float','bool','float','float','bool','bool','bool','float']
config['input']['upper'] = ['','94','','','','','','','']
config['input']['lower'] = ['','45','','','','','','','']

# human and machine readable output descriptions
config['output'] = {}
config['output']['name'] = '4Y risk of Heart Failure'               # kind of risk predicted    '10y CVD risk'
config['output']['outcomeName'] = 'Heart Failure'         # CVD                      'CVD
config['output']['outcomeTime'] = '4'         # in years                 '10'
config['output']['CUI'] = 'C3176374'                # kind of risk CUI          'C3176370'
config['output']['outcomeCUI'] = 'C0018801'          # outcome CUI              'C1716750'

# tabular or machine readable data available for download
config['data'] = {}
config['data']['filename'] = ['']   # name tabular data file     ['All of the Data']
config['data']['fileurl'] = ['']    # some kind of pointer?      ['/var/www/models/99.9999:aaa.a9/all.Rdata']
config['data']['datumname'] = ['Sample Size']  # important data for easy access    ['Sample Size']
config['data']['datum'] = ['15267']      # values for important data         ['8,000,000,000']

# model function and dependencies
config['model'] = {}
config['model']['language'] = 'python'      
config['model']['uncompiled'] = ['model_b.py']  
config['model']['compiled'] = ['']    
config['model']['dependList'] = 'requirements.txt'  
config['model']['example'] = ['example_b.py']    

# I do not know what this would be used for
config['model_category'] = ['prognostic'] 

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
