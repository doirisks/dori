#!/usr/bin/python
# updateconfigs.py
# by Ted Morin
#
# updates all of the configuration files recursively, merges the sql commands into a single file
# set criteria for "configs" at blue lines
# 


import sys
import os

USAGE = 'USAGE: run_scripts_in [DEPTH] [DIRECTORY]'

DEPTH = 2
CURDIR = os.getcwd()
START = CURDIR

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
text = merge_sql_commands(START,0)


# save the merged sql commands in the starting directory
os.chdir(CURDIR)
output = open('merged.sql','w')
output.write(text)
output.close()
