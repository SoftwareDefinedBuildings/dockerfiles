RUN service apache2 start

 Start this by running
```
# inside this folder -- run this once #
sudo docker build -t smap_uot .
# to run a sMAP archiver now #
sudo docker run -p 80:80 -p 8079:8079 -i -t -d smap_uot
sudo docker attach <docker container id>
## inside container ##
$ sudo service postgresql start
$ sudo service apache2 start
$ cd /usr/share/powerdb2
$ python manage.py createsuperuser
$ supervisord -c /etc/supervisor/supervisor.conf
```
You can then detach with `ctl-p + ctl-q`
