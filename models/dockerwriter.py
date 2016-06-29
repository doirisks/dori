#!/usr/bin/python
"""
dockerwriter.py
by Ted Morin

write docker files for python. To build a docker container of a particular compile a docker file 
USAGE: sudo python dockerwriter.py [OPTIONS]

OPTIONS:
-b, --build                 build all docker files
-t, --test                  build just the first docker file

N.B: run models.py and CUIs.py first!
"""

import MySQLdb as db
import json
import sys
import os

def getFileExtension(filename):
    if filename.find(".") == -1:
        return ""
    else :
        return filename[filename.find("."):]

def ignore_files(not_ignored, mypath): # no limit to recursion!
    text = ""
    void = True
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    notfiles = [f for f in os.listdir(mypath) if ( not os.path.isfile(os.path.join(mypath, f)) and f[0] != '.' )]
    onlyfiles.sort()
    for f in onlyfiles:
        if not f in not_ignored :   # if the file is ignored
            text += f               # ignore it
            text += '\n'
        else :              # if the file is necessary
            void = False
    
    for d in notfiles:
        nextlevel = ignore_files(not_ignored,os.path.join(mypath,d))
        if nextlevel[1]:  # if directory is void
            text += d + "/"     # ignore the directory
        else :
            text += nextlevel[0] # if the directory has something interesting in it
    return text, void


# connect to mysql server
cnx = db.connect(host='localhost',db = 'doiarchive', user='doirisks', passwd='bitnami')
cur = cnx.cursor()

# get data on the models
fetch_query = """SELECT id, DOI, language, compiled, uncompiled, dependList, example, config FROM `models`"""
cur.execute(fetch_query)

# save the base, should be the path to ......./dori-master/models
models_path = os.getcwd()

# counter so that progress can be observed, used for -t option
count = 0

# iterate through all of the models
model = cur.fetchone()
while model != None :
    # text of the Dockerfile
    text = ""
    
    # comments
    text += """#######################################################################
# Dockerfile to build model """ + str(model[0]) + """
# Based on continuumio/miniconda, produced by dockerwriter.py
#######################################################################

"""
    # convert model to a python list
    model = list(model)
    
    # expand json strings
    model[3] = json.loads(model[3]) # compiled
    model[4] = json.loads(model[4]) # uncompiled
    model[6] = json.loads(model[6]) # example(s)
    
    # files which will not be ignored
    added = []
    
    ###################################
    # rules for python imports (PART I)
    if model[2][:6] == 'python' or model[2] == 'py':
    
        # FROM statement
        text += 'FROM continuumio/miniconda\n'
        
        # install pip
        text += 'RUN conda install pip\n'
        
        # MAINTAINER statement
        text += 'MAINTAINER "DOI RISKS"\n'
        
        # bring in a duplicate of the first compiled file with a uniform name
        if len(model[3]) != 0:
            text += "COPY ./" + model[3][0] + " model" + getFileExtension(model[3][0]) + '\n'
        
        # bring in a duplicate of the first uncompiled file with a uniform name
        if len(model[4]) != 0 :
            text += "COPY ./" + model[4][0] + " model" + getFileExtension(model[4][0]) + '\n'
        
        # bring in the dependency list if it exists
        if model[5] != None:
            text += "COPY ./" + model[5] + " requirements.txt\n"
            added.append(model[5])
            # loading the listed dependencies 
            text += "RUN conda install -f -q --file requirements.txt\n"
            
    ###################################
    # rules for R imports (PART I)
    elif model[2] == 'R' or model[2] == 'r':
        model = cur.fetchone()
        continue
    
    ###################################
    # rules for unrecognized languages
    else :
        model = cur.fetchone()
        continue
        
    ###################################################################### for ALL languages
    # set the current working directory
    os.chdir( os.path.join(models_path,model[1].replace('/',':')) )

    # bring in the compiled files
    for index, item in enumerate(model[3]):
        if item != "":
            text += "COPY ./" + item + " /" + item + '\n'
            added.append(item)
        
    # bring in the uncompiled files
    for index, item in enumerate(model[4]):
        if item != "":
            text += "COPY ./" + item + " /" + item + '\n'
            added.append(item)
        
    # bring in examples if any
    for example in model[6]:
        if example != "":
            text += "COPY ./" + example + " /" + example + '\n'
            added.append(example)
    
    # bring in the JSON config file (if it exists)
    if model[7] != None:
        text += "ADD ./" + model[7] + " config.json"
        added.append(model[7])
    

    # identify the items added by their individual names 
    for index, item in enumerate(added):
        while os.path.split(item)[-1] != os.path.split(os.path.split(item)[-1])[-1]:
            added[i] = os.path.split(item)[-1]
    # ignore all of the files not added
    ignoretext = ignore_files(added, os.getcwd())[0]
    
        
    # name the output file
    if ('-b' in sys.argv or '--build' in sys.argv):
        # write the dockerignore
        with open('.dockerignore', 'w') as output:
            output.write(ignoretext)
        # write the document name
        output_name = 'Dockerfile'
    elif ('-t' in sys.argv or '--test' in sys.argv) and (count == 1):
        # write the dockerignore for use
        with open('.dockerignore', 'w') as output:
            output.write(ignoretext)
        # write the dockerignore for the record
        with open('dockerignore_' + str(model[0]), 'w') as output:
            output.write(ignoretext)
        # write the document name
        output_name = 'Dockerfile_' + str(model[0])
    else :
        # write the dockerignore
        with open('dockerignore_' + str(model[0]), 'w') as output:
            output.write(ignoretext)
        # write the document name
        output_name = 'Dockerfile_' + str(model[0])
    
    with open( output_name ,'w') as output:
        output.write(text)
        
    # write or make the docker container!
    count += 1
    if ('-b' in sys.argv or '--build' in sys.argv):
        os.system("sudo docker build -t doirisks/model_" + str(model[0]) + " ./")
        print str(count) + " images built!"
    elif ('-t' in sys.argv or '--test' in sys.argv) and (count == 1):
        with open( 'Dockerfile' ,'w') as output:
            output.write(text)
        os.system("sudo docker build -t doirisks/model_" + str(model[0]) + " ./")
        print "Test complete!\n1 Dockerfile written"
    else :
        print str(count) + " Dockerfile(s) written!"
    
    model = cur.fetchone()


