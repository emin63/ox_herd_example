
FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive

# Need to do an apt-get update early on or lots of things won't work.
RUN apt-get update

# Need a few things early on so install them first

RUN apt-get update && \
    apt-get -y install python3 python3-pip redis-server

# Setup the user to run ox_herd making sure to:
#   1. Make the primary group www-data so WSGI works if you later decide
#      to use it. This is helpful since if you "git pull" some new files, 
#      you want them to have group www-data so the WSGI web server can 
#      read them.
#   2. Setup profile properly
RUN useradd -ms /bin/bash ox_user && \
  usermod -g www-data ox_user && \
  usermod -a -G www-data ox_user && \

# Setup log directory and pull in setup items.

WORKDIR /home/ox_user/ox_server

# Next add the ox_herd directory we are running from
COPY . ox_herd_example

RUN pip3 install -r ./ox_herd_example/requirements.txt

RUN mkdir -p /home/ox_user/ox_server/logs

ADD ./server_start.sh /ox_server/

# In case you are running docker on windows, need to make sure
# you strip the \r out of the start script
RUN sed -i.bak 's/\r$//' /ox_server/server_start.sh

RUN chmod ugo+rx /ox_server/server_start.sh

RUN chown -R ox_user:www-data /home/ox_user

WORKDIR /ox_server

CMD ["bash", "/ox_server/server_start.sh"]