#!/bin/bash
#####################################
# dorihub.sh
# by Ted M
#
# setup script for a linode/lamp docker container
#

# update the container to make installation possible
sudo apt-get update

# install git and pull to a known directory
sudo apt-get install -y git
mkdir /home/dori-master
cd /home/dori-master
git init
git remote add origin https://github.com/doirisks/dori.git
git pull origin master

# install necessary python (condense to a requirements.txt or .yml or something?)
sudo apt-get install -y python2.7
sudo apt-get install -y python-sql
sudo apt-get install -y python-MySQLdb

# start mysql server
sudo service mysql start

# make a small sql command file, run it, and delete it
# maybe do this step with python instead?
echo "CREATE DATABASE doiarchive ; CREATE USER doirisks@localhost IDENTIFIED BY 'bitnami'; GRANT ALL PRIVILEGES ON doiarchive.* TO 'doirisks'@'localhost';" > sqlsetup.sql
mysql -u root -p"Admin2015" < sqlsetup.sql
rm sqlsetup.sql                                     

# run setup scripts individually
cd setup
./setup.sh
