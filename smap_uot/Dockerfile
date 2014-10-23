FROM sdbase
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get install -y python-software-properties software-properties-common
RUN /usr/bin/add-apt-repository ppa:cal-sdb/smap
RUN apt-get update
RUN apt-get install -y python-smap readingdb postgresql apache2
RUN service postgresql start && service apache2 start && yes no | apt-get install -y powerdb2
CMD /bin/bash
