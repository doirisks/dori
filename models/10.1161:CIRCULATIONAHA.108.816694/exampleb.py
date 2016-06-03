"""
exampleb.py
by Ted Morin

contains example code for 30-year CVD calculator
10.1161/CIRCULATIONAHA.108.816694
2009 Predicting the Thirty-year Risk of Cardiovascular Disease
The Framingham Heart Study
"""

from modelb import model as b

bscores = []
bscores.append( b(1,53,125,1,0,1,161,55) ) #m,53yrs,125sbp,treated,nosmokes, diabetic,161tot,55hdl,bmi20
bscores.append( b(0,61,124,0,1,0,180,47) ) #f,61yrs,124sbp,not treated,smokes,not db,180tot,47hdl,bmi20
bscores.append( b(1,55,118,0,1,1,200,45) ) #m, 55yrs,118sbp, not treated, smokes, db, 200tot, 45hdl,bmi20
bscores.append( b(1,45,129,1,0,1,220,56) ) #m, 45, 129sbp, treated, nosmokes, db, 220tot, 56hdl,bmi20
bscores.append( b(1,71,125,0,1,0,205,47) ) #m, 71,  125sbp, notreated,  smokes, nodb,205tot, 47hdl,bmi20
bscores.append( b(0,40,117,0,0,1,160,54) ) #f, 40, 117sbp, notreated, nosmokes, db, 160, 54hdl,bmi20
bscores.append( b(0,43,127,1,0,1,300,67) ) #f, 43, 127sbp, treated, nosmokes, db, 300, 67hdl,bmi20
bscores.append( b(0,52,112,1,1,1,287,56) ) #f, 52, 112sbp, treated, smokes,db, 287, 56hdl,bmi20
bscores.append( b(0,61,141,0,1,0,371,80) ) #f, 61, 141sbp,notreated, smokes,no db, 371tot,80hdl,bmi20
bscores.append( b(0,46,131,0,1,0,211,87) ) #f, 46yrs, 131sbp, notreated,smokes,no db, 211tot,87hdl,bmi20
bscores.append( b(1,39,135,0,0,0,170,60) ) #m, 39yrs, 135sbp, notreated, no smoke, no db, 170tot, 60hdl,bmi20

for i in range(len(bscores)):
    print "%.3f" % (float(bscores[i])*100.)
