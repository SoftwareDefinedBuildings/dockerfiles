FROM ubuntu:12.10
MAINTAINER Michael Andersen <michael@steelcode.com>

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y python-setuptools build-essential python-dev mercurial vim
RUN easy_install pip

#--------------
#Readingdb deps
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x /usr/sbin/policy-rc.d
RUN apt-get install -y libdb5.3-dev libprotobuf-dev libprotoc-dev zlib1g-dev python-numpy swig postgresql git autoconf libtool check libprotobuf-c0-dev protobuf-c-compiler pkg-config postgresql postgresql-contrib python-psycopg2
 
#Get some sources
RUN mkdir /srv/src
RUN git clone https://github.com/SoftwareDefinedBuildings/readingdb.git /srv/src/readingdb
RUN cd /srv/src/readingdb && git checkout adaptive
RUN git clone https://github.com/SoftwareDefinedBuildings/smap.git /srv/smap
#Not that this is for the unitoftime experimental branch
RUN cd /srv/smap && git checkout unitoftime

#Make some sources
RUN cd /srv/src/readingdb && autoreconf --install && ./configure --prefix=/ && make && make install && cd src && make && make install
RUN cd /srv/src/readingdb/python && make && make install 
ADD . /srv/repo
RUN cd /srv/repo && ./mk_archiver.sh
RUN cd /srv/smap/python && python setup.py install
RUN mkdir -p /etc/smap
RUN cp /srv/smap/python/conf/archiver.ini /etc/smap/

RUN mkdir -p /srv/smap_archiver/rdb

RUN apt-get install -y supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN apt-get install -y openssh-server curl python-pycurl python-twisted 
RUN apt-get install -y libcurl4-openssl-dev apache2 python-twisted python-scipy apache2-utils libapache2-mod-python python-openssl libapache2-mod-wsgi 
RUN pip install ply zope.interface avro configobj python-dateutil httplib2 pycurl pandas
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN cd /srv/smap/python && python setup.py install


