
FROM ubuntu:12.10

ADD nagios-4.0.2.tar.gz /root/
ADD nagios-plugins-1.5.tar.gz /root/

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y apache2 libapache2-mod-php5 build-essential libgd2-xpm-dev vim python-setuptools openssh-server supervisor
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor

RUN useradd nagios
RUN groupadd nagcmd
RUN usermod -a -G nagcmd nagios
RUN usermod -a -G nagcmd www-data

RUN cd /root/nagios-4.0.2/ && ./configure --with-command-group=nagcmd
RUN cd /root/nagios-4.0.2/ && make -j8 all && make install && make install-init && make install-config && make install-commandmode

ADD contacts.cfg /root/

RUN cp /root/contacts.cfg /usr/local/nagios/etc/objects/

RUN cd /root/nagios-4.0.2/ && make install-webconf
RUN echo "nagiosadmin:\$apr1\$ifq5qZW9\$lw45Fo.ww/JfYIBnOFGnr." > /usr/local/nagios/etc/htpasswd.users

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN cd /root/nagios-plugins-1.5/ && ./configure --with-nagios-user=nagios --with-nagios-group=nagios
RUN cd /root/nagios-plugins-1.5/ && make -j8 && make install

EXPOSE 80
RUN sed -i '/root:/c\root:$6$kLl9tkp4$UOSiGotOpXQJY1nncvLBFvUZwgaJkKq1rqZUklQtwKrh.NH5lus0IY9Rtb0xzMGEHb8xqrm6PLUh63ViODCrK1:16093:0:99999:7:::' /etc/shadow 
CMD ["/usr/bin/supervisord"]
