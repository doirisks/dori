#!/usr/bin/python
# updateconfigs.py
# by Ted Morin
#
# updates all of the configuration files recursively
# set criteria for "configs" at blue line


import sys
from os import *
from os.path import isfile, isdir, join

USAGE = 'USAGE: run_scripts_in [DEPTH] [DIRECTORY]'

DEPTH = 1
START = getcwd()


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
        if isdir(sys.argv[2]):
            START = sys.argv[2]
        else :                                  # invalid directory
            print USAGE
            print 'ERROR: directory invalid'

# actual process here...
def run_scripts_in(mypath,recurs):
    if recurs == DEPTH: return      #set depth here
    count = 0
    print mypath
    chdir(mypath)
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    notfiles = [f for f in listdir(mypath) if ( not isfile(join(mypath, f)) and f[0] != '.' )]
    onlyfiles.sort()
##############################################################################################################
    for f in onlyfiles:
        if f[:5] == "new_c" and f[-3:] == '.py':
            print join(mypath, f)
            system('python "' + join(mypath, f) + '"')
            count += 1
    
    for d in notfiles:
         run_scripts_in(join(mypath,d),recurs+1)
    print count
    print

run_scripts_in(START,0)



