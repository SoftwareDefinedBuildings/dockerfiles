FROM ubuntu:12.10

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y apt-mirror apache2 vim supervisor

ADD mirror.list /etc/apt/mirror.list
RUN echo "0 4     * * *   apt-mirror      /usr/bin/apt-mirror > /var/spool/apt-mirror/var/cron.log" > /etc/cron.d/apt-mirror
RUN ln -s /var/spool/apt-mirror/mirror/archive.ubuntu.com/ubuntu /var/www/ubuntu
RUN sed -i '/root:/c\root:$6$kLl9tkp4$UOSiGotOpXQJY1nncvLBFvUZwgaJkKq1rqZUklQtwKrh.NH5lus0IY9Rtb0xzMGEHb8xqrm6PLUh63ViODCrK1:16093:0:99999:7:::' /etc/shadow 
CMD ["/usr/bin/supervisord"]
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN apt-get install -y openssh-server
