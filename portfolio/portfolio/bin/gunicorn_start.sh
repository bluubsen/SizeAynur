#!/bin/bash

NAME="aynurotyakmaz"                                     # Name of the application
DJANGODIR=/var/www/aynurotyakmaz.com                     # Django project directory
SOCKFILE=/var/www/aynurotyakmaz.com/bin/gunicorn.sock    # we will communicte using this unix socket
USER=dylan                                        # the user to run as
GROUP=unused                                      # the group to run as
NUM_WORKERS=2                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=portfolio.settings.production # which settings file should Django use
DJANGO_WSGI_MODULE=portfolio.wsgi                    # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $DJANGODIR/.venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR/.venv/bin/lib/python3.6

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
cd $NAME
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
--log-file=/var/www/dylanh.net/logs/gunicorn.log
