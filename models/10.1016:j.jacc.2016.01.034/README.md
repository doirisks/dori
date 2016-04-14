# 10.1016/j.jacc.2016.01.034
Spontaneous MI After Non–ST-Segment Elevation Acute Coronary Syndrome Managed Without Revascularization
The TRILOGY ACS Trial

## RESTful API
This model is also availble via RESTful API as follows (assuming Python):
Find out what the input of the model is:
```
import requests
#Query model metadata
r = requests.get('http://colab-sbx-322.oit.duke.edu:49167/tril_info')
r.text

```

Score Actual data:
```
import requests
r2 = requests.post('http://colab-sbx-322.oit.duke.edu:49167/tril_score', data = {'CREATCN_IMP':1.5,
                      'creatcn_imp85':0.65,
                      'N_PPIRD':1,
                      'N_STATINRD':1,
                      'NSTEMI':1,
                      'KILLIP1_IMP':1,
                      'AGEYR':85,
                      'N_MHDIAB_IMP':1,
                      'N_MHHYP_IMP':1,
                      'N_MHCAD_IMP':0,
                      'N_CANGIO_IMP':0,
                      'SMOKE30_IMP':1,
                      'N_MHHLP_IMP':1,
                      'N_MHPAD_IMP':0,
                      'N_MHPMI_IMP':1,
                      'N_MHCHF_IMP':0,
                      'N_MHPPCI_IMP':1,
                      'N_MHPCABG_IMP':0})
r2.content
```
