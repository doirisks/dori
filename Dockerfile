#####################################
# doirisks/dori
# by Ted M
#
#####################################

FROM ubuntu:14.04
MAINTAINER "DOI RISKS"

ADD . /src

# update the container to make installation possible
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5-mysql

# install necessary python (condense to a requirements.txt or .yml or something?)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-sql
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-MySQLdb
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-numpy

# install R?
#TODO

RUN DEBIAN_FRONTEND=noninteractive bash /src/setup/dockersetup.sh

