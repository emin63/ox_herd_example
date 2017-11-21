#!/bin/sh

# This is a script used to start everything up on docker.

# Restart redis server just to make sure it is up and working.
/etc/init.d/redis-server restart

# Start the rq worker and rqscheduler processes piping their output to logs
su - -c "rq worker" ox_user 2>&1 | \
   rotatelogs /home/ox_user/ox_server/logs/rq_worker.log 86400 10M &
su - -c rqscheduler ox_user 2>&1 | \
   rotatelogs /home/ox_user/ox_server/logs/rqscheduler.log 86400 10M&

# Set and echo PYTHONPATH for clarity
export PYTHONPATH=/home/ox_user/ox_server/ox_herd_example
echo "PYTHONPATH is $PYTHONPATH"

# Start the server
su - -c "python3 /home/ox_user/ox_server/ox_herd_example/app.py" ox_user
