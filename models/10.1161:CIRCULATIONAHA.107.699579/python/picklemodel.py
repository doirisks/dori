"""
picklemodel.py
by Ted Morin

pickles model from 10.1161/CIRCULATIONAHA.107.699579 and prints test outputs
"""

import cPickle as pickle


#pickles function
import model as m
model_obj = open("model_obj.p",'wb')
pickle.dump(m.model, model_obj)
model_obj.close()

#unpickles function
model_obj = open("model_obj.p","rb")
model = pickle.load( model_obj )
model_obj.close()

#tests
print model(1,1,53,161,55,125,0,1) #m,treated,53yrs,161tot,55hdl,125sbp,nosmokes, diabetic
print model(0,0,61,180,47,124,1,0) #f,not treated,61yrs,180tot,47hdl,124sbp,smokes,not db
print model(1,0,55,200,45,118,1,1) #m, not treated, 55yrs, 200tot, 45hdl, 118sbp, smokes, db
print model(1,1,45,220,56,129,0,1) #m, treated, 45, 220tot, 56hdl, 129sbp, nosmokes, db
print model(1,0,71,205,47,125,1,0) #m, notreated, 71, 205, 47hdl, 125sbp, smokes, nodb
print model(0,0,40,160,54,117,0,1) #f, notreated, 40, 160, 54hdl, 117sbp, nosmokes, db
print model(0,1,43,300,67,127,0,1) #f, treated, 43, 300, 67hdl, 127sbp, nosmokes, db
print model(0,1,52,287,56,112,1,1) #f, treated, 52, 287, 56hdl, 112sbp,smokes,db
print model(0,0,61,371,80,141,1,0) #f, notreated, 61,371tot,80hdl,141sbp,smokes,no db
print model(0,0,46,211,87,131,1,0) #f, notreated, 46yrs,211tot, 87hdl,131sbp,smokes,no db
print model(1,0,39,170,60,135,0,0) #m, notreated, 39yrs, 170tot, 60hdl, 135sbp, no smoke, no db



