#!/bin/bash
#####################################
# dorihub.sh
# by Ted M
#
# setup script for a ubuntu:14.04 docker container
# apache2 and mysql must started in docker container (for now)

# start mysql server
service mysql start

# run setup scripts
cd /src/setup
./dockersetup.py
./setup.sh

# set interface as the default webpage of the server
cp -r /src/interface /var/www/interface
mkdir /var/www/interface/log
chmod -R 755 /var/www/interface
sed -i "s/\/var\/www\/html/\/var\/www\/interface\/public/g" /etc/apache2/sites-available/000-default.conf
cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/interface.conf
a2dissite 000-default.conf 
rm /etc/apache2/sites-available/000-default.conf 
a2ensite interface.conf
chmod -R 755 /src/interface/

# stop the mysql server
service mysql stop
