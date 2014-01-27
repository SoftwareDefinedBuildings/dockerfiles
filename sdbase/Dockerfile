
FROM ubuntu:12.10
MAINTAINER Michael Andersen <m.andersen@cs.berkeley.edu>

RUN echo "deb http://ubuntu.cal-sdb.org/ubuntu quantal main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y

#Set the root password
RUN sed -i '/root:/c\root:$6$kLl9tkp4$UOSiGotOpXQJY1nncvLBFvUZwgaJkKq1rqZUklQtwKrh.NH5lus0IY9Rtb0xzMGEHb8xqrm6PLUh63ViODCrK1:16093:0:99999:7:::' /etc/shadow 

RUN apt-get install -y python-pip
RUN pip install supervisor

RUN mkdir -p /var/run
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d
ADD supervisord.conf /etc/supervisord.conf
