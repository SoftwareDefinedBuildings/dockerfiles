#Use the archiver image
FROM smap_archiver

#RUN apt-get install -y python-setuptools build-essential python-dev mercurial vim monit
#RUN easy_install pip
#--------------
#Readingdb deps
#RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x /usr/sbin/policy-rc.d
#RUN apt-get install -y libdb5.3-dev libprotobuf-dev libprotoc-dev zlib1g-dev python-numpy swig postgresql git autoconf libtool check libprotobuf-c0-dev protobuf-c-compiler pkg-config postgresql postgresql-contrib python-psycopg2
 
#Powerdb2 deps
RUN apt-get install -y libcurl4-openssl-dev apache2 python-twisted python-scipy apache2-utils libapache2-mod-python python-openssl python-django python-flup libapache2-mod-wsgi 
RUN pip install twisted ply zope.interface avro configobj python-dateutil httplib2 django-piston pycurl

#Get some sources
#RUN mkdir /srv/src
#RUN git clone git://github.com/stevedh/readingdb.git /srv/src/readingdb
#RUN svn checkout http://smap-data.googlecode.com/svn/trunk/ /srv/smap
#RUN svn checkout http://smap-data.googlecode.com/svn/branches/powerdb2 /srv/powerdb2
RUN git clone https://github.com/SoftwareDefinedBuildings/powerdb2.git /srv/powerdb2
ADD . /srv/repo

#Utility scripts for stuff that Docker can't do

#Make some sources
RUN cp /srv/repo/powerdb2_site /etc/apache2/sites-available
RUN cd /etc/apache2/sites-enabled && rm * && ln -s ../sites-available/powerdb2_site powerdb2_site
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN cd /srv/repo && ./mk_django.sh
RUN cd /srv/repo && ./bootstrap_subkey.sh
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /bin/bash
#Need to run the following in the container:
# cd /srv/powerdb2/
# python manage.py changepassword root


