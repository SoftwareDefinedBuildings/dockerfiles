FROM stackbrew/ubuntu:13.10
MAINTAINER Michael Andersen <m.andersen@cs.berkeley.edu>

RUN echo "deb http://miranda.cs.berkeley.edu:8080/ubuntu saucy main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y openssh-server python python-setuptools python-pip python-dev

# fix openssh
RUN sed -i '/session\s*required\s*pam_loginuid.so/c\session optional pam_loginuid.so/' /etc/pam.d/sshd
RUN echo 'LANG="en_US.UTF-8"' >> /etc/default/local

#Set the root password
RUN sed -i '/root:/c\root:$6$kLl9tkp4$UOSiGotOpXQJY1nncvLBFvUZwgaJkKq1rqZUklQtwKrh.NH5lus0IY9Rtb0xzMGEHb8xqrm6PLUh63ViODCrK1:16093:0:99999:7:::' /etc/shadow 

RUN pip install supervisor

RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d
ADD supervisord.conf /etc/supervisord.conf


