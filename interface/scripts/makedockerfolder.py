#!/usr/bin/python
"""
makedockerfolder.py
by Ted Morin

populate a folder with Dockerfile and appropriate files for a particular model
based on functions from dockerwriter.py
"""


DYNAMIC_CONTENT_DIRECTORY = "/var/www/interface/public/dynamic"     # path to directory 
                                            # where dynamic content will be stored temporarily

DOCKHASH_MIN = 1000                         # starting and maximum hashes for dynamic content
DOCKHASH_MAX = 9999
MODELS_PATH = "/src/models"                 # path to models directory in source

# basic imports
import os
import sys
import random

# mid-import error check
if len(sys.argv) < 2:
    print "error"
    exit()

# imports for retrieving connection info from dockerwriter
import imp
import string

# imports for interacting with the database
import MySQLdb as db
import json

# a function to get a file extension
def getFileExtension(filename):
    if filename.find(".") == -1:
        return ""
    else :
        return filename[filename.find("."):]

# populate the target directory with the added files from the current working directory, screens blanks
def populate(added, target):
    current_working_directory = os.getcwd()
    target = os.path.abspath(target)
    for item in added:
        if item != "":
            start = os.path.join(current_working_directory, item)
            #print start
            end = os.path.join(target, item)
            #print end
            if os.path.isdir(start):
                os.system('cp -r "' + start + '" "' + end + '"') 
            else :
                os.system('cp "' + start + '" "' + end + '"') 
            # consider using -l (link) for the cp command
            # this option might speed up the process and save disk space, esp for bigger models
            # how would docker build react?

# dockbuild([id, DOI, language, compiled, uncompiled, dependList, example, config])
# prepares a tar.gz with all necessary parts and the Dockerfile
# must be run from the model's DOI directory after Dockerfile has been built
# requires root privileges to run (?)
def dockprepzip(model, dynamic_content):
    dynamic_content = os.path.abspath(dynamic_content)
    
    # create a unique directory for this call
    dockhash = 1000
    dockpath = os.path.join( dynamic_content, str(dockhash) )
    while os.path.isdir(dockpath) :
        dockhash += 1
        # limit the number of model requests that can exist in the queue
        if dockhash > DOCKHASH_MAX:
            print("error")
            exit()
        dockpath = os.path.join( dynamic_content, str(dockhash) )
    os.system("mkdir " + dockpath)
    
    # files which will be included in the container
    added = []
    
    # add the compiled files
    for item in model[3]:
        if item != "":
            added.append(item)
        
    # add the uncompiled files
    for item in model[4]:
        if item != "":
            added.append(item)
            
    # add the dependency list if it exists
    if model[5] != None and model[5] != "":
        added.append(model[5])
        
    # add examples if any
    for example in model[6]:
        if example != "":
            added.append(example)
    
    # add the JSON config file (if it exists)
    if model[7] != None and model[7] != "":
        added.append(model[7])
    
    # populate the folder from which the docker container will be built
    populate(added, dockpath)
   
    # move in the Dockerfile if it exists
    if os.path.isfile(   os.path.join(os.getcwd(), "Dockerfile_"+ str(model[0]))   ):
        os.system("cp Dockerfile_"+ str(model[0]) + " " + dockpath + "/Dockerfile")
    else :
        print("error")
        exit()

    # make sure that there is no / at the end of the dockpath
    if (dockpath[-1] == '/'):
        dockpath = dockpath[:-1]

    # zip the folder
    os.system("tar cfz " + dockpath + ".tar.gz -C " + dockpath + " .")
    # remove the folder
    #os.system("rm -rf " + dockpath)

    # return the dockhash
    return(dockhash)

# import from dockerwriter (hard coded)
conn_conf = imp.load_source("/src/setup/connection_config", "connection_config", open("/src/setup/connection_config.py", 'r') )

# connect to mysql server
cnx = db.connect(host=conn_conf.DEFAULT_HOSTNAME,db = conn_conf.DEFAULT_DATEBASE, user=conn_conf.DEFAULT_USERNAME, passwd=conn_conf.DEFAULT_PASSWORD)
cur = cnx.cursor()

# get data on the models
fetch_query = """SELECT id, DOI, language, compiled, uncompiled, dependList, example, config FROM `models` WHERE id = """ + sys.argv[1]
cur.execute(fetch_query)

# get the model
model = cur.fetchone()

# close the cursor and the connection
cur.close()
cnx.close()

# error check - is the id valid?
if model == None:
    print "error"
    exit()

# convert model to a python list
model = list(model)

# expand json strings
model[3] = json.loads(model[3]) # compiled
model[4] = json.loads(model[4]) # uncompiled
model[6] = json.loads(model[6]) # example(s)

# set the current working directory to the target DOI
os.chdir( os.path.join(MODELS_PATH,model[1].replace('/',':')) )

# build the model
dockhash = dockprepzip(model,DYNAMIC_CONTENT_DIRECTORY)

print(dockhash)
