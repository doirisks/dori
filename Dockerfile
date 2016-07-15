#####################################
# doirisks/dori
# by Ted M
#
#####################################

FROM doirisks/doribase
MAINTAINER "DOI RISKS"

ADD . /src

RUN DEBIAN_FRONTEND=noninteractive bash /src/setup/dockersetup.sh

