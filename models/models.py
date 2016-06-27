#!/usr/bin/python
"""
populateCUIs.py
by Ted Morin

builds the 'models' table in doiarchives from config.py files

N.B: relies on "new_config_gener.py" files in model directories
"""


import MySQLdb as db
import json
import sys
import os

# configuration
cnx = db.connect(host = 'localhost',user='doirisks',passwd='bitnami',db='doiarchive')

cur2 = cnx.cursor()
# refresh the table
refresh_query = """-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: doiarchive
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

DROP TABLE IF EXISTS `models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  `outcometime` varchar(3),
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
  
  `modified` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
/*  `uploaded` DATE DEFAULT CURRENT_DATE,*/
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

"""
cur2.execute(refresh_query)
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
CURDIR = os.getcwd()
START = CURDIR

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

# running scripts
def run_scripts_in(mypath,recurs):
    if recurs == DEPTH: return   
    count = 0
    print mypath
    os.chdir(mypath)
    
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    notfiles = [f for f in os.listdir(mypath) if ( not os.path.isfile(os.path.join(mypath, f)) and f[0] != '.' )]
    onlyfiles.sort()
##############################################################################################################
    for f in onlyfiles:
        if f[:5] == "new_c" and f[-3:] == '.py':        # change this line if lines are changed
            print os.path.join(mypath, f)
            os.system('python "' + os.path.join(mypath, f) + '"')
            count += 1
    
    for d in notfiles:
         run_scripts_in(os.path.join(mypath,d),recurs+1)
    print count
    print

# combining sql commands
def merge_sql_commands(mypath,recurs):
    text = ""
    if recurs == DEPTH: return text
    
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    notfiles = [f for f in os.listdir(mypath) if ( not os.path.isfile(os.path.join(mypath, f)) and f[0] != '.' )]
    onlyfiles.sort()
##############################################################################################################
    for f in onlyfiles:
        if f[:5] == "confi" and f[-4:] == '.sql':
            infile = open(os.path.join(mypath, f),'r')
            text += infile.read()
            infile.close()
            text += ';\n'
    
    for d in notfiles:
        text += str(merge_sql_commands(os.path.join(mypath,d),recurs+1))
    
    return text
    
# run the scripts
run_scripts_in(START,0)

os.chdir(CURDIR)
# get the commands
insert_query = merge_sql_commands(START,0)
insert_query += "COMMIT;\n"

#print insert_query
#print len(CUIs.keys())

cur3.execute(insert_query)

cur3.close()
cnx.close()
