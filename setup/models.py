#!/usr/bin/python
"""
populateCUIs.py
by Ted Morin

builds the 'models' table in doiarchives from config.py files

N.B: relies on "config_gener*.py" files in model directories
"""

from connection_config import *
import MySQLdb as db
import json
import sys
import os
import subprocess

# configuration
cnx = db.connect(host = DEFAULT_HOSTNAME,user=DEFAULT_USERNAME,passwd=DEFAULT_PASSWORD,db=DEFAULT_DATEBASE)

# refresh the table
"""-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (i686)
--
-- Host: dori_mysql    Database: doiarchive
-- ------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `models`
--
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;"""
refresh_query = """DROP TABLE IF EXISTS `models`;
CREATE TABLE `models` (

  `id` int(16) NOT NULL AUTO_INCREMENT, /*id category*/
  `DOI` varchar(255)  COLLATE utf8_unicode_ci NOT NULL,
  `papertitle` varchar(255) NOT NULL,
  `modeltitle` varchar(255) NOT NULL,
  `yearofpub` int(16),
  `authors` TEXT,

  `must` TEXT, /*population category*/
  `mustnot` TEXT,
  `mustCUI` TEXT,
  `mustnotCUI` TEXT,

  `inpname` TEXT, /*input category*/
  `inpdesc` TEXT,
  `inpCUI` TEXT,
  `inpunits` TEXT,
  `inpdatatype` TEXT,
  `upper` TEXT,
  `lower` TEXT,
  `numofinputs` int(8),
  
  `output` varchar(255), /*output category*/
  `outcome` varchar(255),
  `outcometime` varchar(8),
  `outputCUI` varchar(255),
  `outcomeCUI` varchar(255),
  
  `filename` TEXT, /*data category*/
  `filepointer` TEXT,
  `datumname` TEXT,
  `datum` TEXT,
  
  `language` varchar(12), /*model category*/
  `uncompiled` TEXT,
  `compiled` TEXT,
  `dependList` varchar(255),
  `example` TEXT,
  
  `model_category` varchar(255), /*other categories: model_category and predictive ability*/
  `type` varchar(255), 
  `metric` varchar(255), 
  `value` varchar(255), 
  `lcl` varchar(255), 
  `ucl` varchar(255), 
  `config` varchar(255),
  
  `modified` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
/*  `uploaded` DATE DEFAULT CURRENT_DATE,*/
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci

"""
for sql in refresh_query.split(";"): #given file, may need ";\n"
    cur2 = cnx.cursor()
    cur2.execute(sql)
    cur2.close()

cur3 = cnx.cursor()
# build the insert query

#vestiges of earlier script
"""
#!/usr/bin/python
# updateconfigs.py
# by Ted Morin
#
# updates all of the configuration files recursively, merges the sql commands into a single file
# set criteria for "configs" at blue lines
# 
"""

USAGE = 'USAGE: run_scripts_in [DEPTH] [DIRECTORY]'

DEPTH = 2
models_path = os.path.abspath(os.path.join(os.getcwd(),"../models"))
START = models_path
os.chdir(models_path)

"""
# input checks
if len(sys.argv) > 3:                           # too many arguments
    print USAGE
    print "ERROR: too many arguments"
    exit(1)
elif 1 < len(sys.argv):                         # more than one argument
    try :
        DEPTH = int(sys.argv[1])
    except :                                    # non-integer depth
        print USAGE
        print "ERROR: non-integer depth"
        exit(1)
    if len(sys.argv) == 3:
        if os.path.isdir(sys.argv[2]):
            START = sys.argv[2]
        else :                                  # invalid directory
            print USAGE
            print 'ERROR: directory invalid'
"""

# runs scripts and returns the a list of "rows" for the db
def run_scripts_in(mypath,recurs):
    if recurs == DEPTH: return ""
    rows = []
    count = 0
    #print mypath
    os.chdir(mypath)
    
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    onlyfiles.sort()
    notfiles = [f for f in os.listdir(mypath) if ( not os.path.isfile(os.path.join(mypath, f)) and f[0] != '.' )]
    notfiles.sort()
    for f in onlyfiles:
        # identify "config_gener" files
        if f[:12] == "config_gener" and f[-3:] == '.py':
            thefile = os.path.join(mypath, f)
            #print(thefile)
            p = subprocess.Popen(['python', thefile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            configfile, errors = p.communicate()    # expects the full configfile name returned
            if configfile[-1] == "\n":
                configfile = configfile[:-1]
            print errors    # print any errors
            with open(os.path.join(mypath, configfile), 'r') as inpfile :
                config = json.load(inpfile)
                
                # build the query
                import sql

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

                    config['config'],
                    
                    len(config['input']['CUI'])
                ]
                rows.append(modvalues)
                
                # make sure that the outcome time is short enough
                if len(modvalues[18]) > 8:
                    modvalues[18] = modvalues[18][:8]
                
                count += 1
    
    for d in notfiles:
        rows += run_scripts_in(os.path.join(mypath,d),recurs+1)
    
    #print(count)
    return(rows)

# run the scripts and collect values
insert_rows = run_scripts_in(START,0)

# build a template
modcolumns = ["DOI", "papertitle", "modeltitle", "yearofpub", "authors", "must", "mustnot", "mustCUI", "mustnotCUI", "inpname", "inpdesc", "inpCUI", "inpunits", "inpdatatype", "upper", "lower", "output", "outcome", "outcometime", "outputCUI", "outcomeCUI", "filename", "filepointer", "datumname", "datum", "language", "uncompiled", "compiled", "dependList", "example", "model_category", "type", "metric", "value", "lcl", "ucl", "config", "numofinputs"]
columns = """`, `""".join(modcolumns)
values_template = """', '""".join(["""'%s'"""] * len(modcolumns)) # strings are quoted previously
inserttemplate = """INSERT INTO models (`%s`) values ('%s')""" % (columns, values_template)

for row in insert_rows:
    cur3.execute(inserttemplate, *row)

cur3.execute("COMMIT")

# clear result sets (https://github.com/farcepest/MySQLdb1/issues/28)
#while cur3.nextset():
#    # debugging print:
#    print('threw out a result set')
#    pass

cur3.close()
cnx.close()

#print insert_query
print "models inserted: " + str( (len(insert_query.split('\n')) - 2)/ 2)

