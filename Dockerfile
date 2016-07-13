#####################################
# doirisks/dori
# by Ted M
#
#####################################

FROM linode/lamp
MAINTAINER "DOI RISKS"

ADD . /src
RUN sudo bash /src/setup/dockersetup.sh

