#####################################
# doirisks/doribase
# by Ted M
#
# the docker image from which the dori image should be built
# pre-installs apache and python packages (and R?) for the dori docker
#####################################

FROM ubuntu:14.04
MAINTAINER "DOI RISKS"

# update the container to make installation possible
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5-mysql

# install necessary python (condense to a requirements.txt or .yml or something?)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-sql
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-MySQLdb
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-numpy

# install R
ADD https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh ./Miniconda2-latest-Linux-x86_64.sh
RUN DEBIAN_FRONTEND=noninteractive bash Miniconda2-latest-Linux-x86_64.sh -b -p /bin/miniconda;
# add /bin/miniconda/bin to PATH in /root/.bashrc, /var/www/.bashrc, and /etc/apache2/envvar
RUN DEBIAN_FRONTEND=noninteractive echo 'export PATH="/bin/miniconda/bin:$PATH"' >> ~/.bashrc; echo 'export PATH="/bin/miniconda/bin:$PATH"' >> /var/www/.bashrc; echo 'export PATH="/bin/miniconda/bin:$PATH"' >> /etc/apache2/envvars
RUN DEBIAN_FRONTEND=noninteractive /bin/miniconda/bin/conda update -y conda
RUN DEBIAN_FRONTEND=noninteractive /bin/miniconda/bin/conda install -y -c r r

# install non-automatic python libraries
RUN DEBIAN_FRONTEND=noninteractive /bin/miniconda/bin/conda install -y numpy
RUN DEBIAN_FRONTEND=noninteractive /bin/miniconda/bin/conda install -y MySQL-python
RUN DEBIAN_FRONTEND=noninteractive yes | /bin/miniconda/bin/pip install python-sql # I do not like this hack

