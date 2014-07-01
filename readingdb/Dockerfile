FROM mubuntu

RUN apt-get install -y python-setuptools build-essential python-dev mercurial vim
RUN easy_install pip

#--------------
#Readingdb deps
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x /usr/sbin/policy-rc.d
RUN apt-get install -y libdb5.3-dev libprotobuf-dev libprotoc-dev zlib1g-dev python-numpy swig git autoconf libtool check libprotobuf-c0-dev protobuf-c-compiler pkg-config
 
#Get some sources
RUN mkdir /srv/src
RUN git clone https://github.com/SoftwareDefinedBuildings/readingdb.git /srv/src/readingdb
RUN cd /srv/src/readingdb && git checkout adaptive
RUN git clone https://github.com/SoftwareDefinedBuildings/smap.git /srv/smap
RUN cd /srv/smap

#Make some sources
RUN cd /srv/src/readingdb && autoreconf --install && ./configure --prefix=/ && make && make install && cd src && make && make install
RUN cd /srv/src/readingdb/python && make && make install 
ADD . /srv/repo

RUN mkdir -p /srv/smap_archiver/rdb

RUN apt-get install -y supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN cd /srv/smap/python && python setup.py install
#RUN cd /srv/repo && ./bootstrap_subkey.sh

EXPOSE 4242
CMD ["/usr/bin/supervisord"]


