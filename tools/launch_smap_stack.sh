
#First we would launch the data container
docker run -d -t -i -name smap_data -v /srv/smap_archiver/ busybox /bin/sh

#Then launch an archiver connected to it
docker run -p 8079 -d --volumes-from smap_data smap_archiver supervisord
