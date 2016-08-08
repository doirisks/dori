#!/bin/bash
#####################################
# dorihub.sh
# by Ted M
#
# setup script for runnign dori in the doirisks/dori docker container

# run setup scripts
#cd /src/setup
#./setup.sh

# set interface as the default webpage of the server
cp -r /src/interface /var/www/interface
mkdir /var/www/interface/log
chmod -R 755 /var/www/interface
sed -i "s/\/var\/www\/html/\/var\/www\/interface\/public/g" /etc/apache2/sites-available/000-default.conf
cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/interface.conf
a2dissite 000-default.conf 
rm /etc/apache2/sites-available/000-default.conf 
a2ensite interface.conf
#chmod -R 755 /src/interface/ # unnecessary
chown -R www-data:www-data /var/www/interface/

