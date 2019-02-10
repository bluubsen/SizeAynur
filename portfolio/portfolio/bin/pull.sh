URL="aynurotyakmaz.com"
PROJECT="portfolio"

GIT_LOGIN="dylanpeterhayward"
GIT_PASS="oFZ72cQNzq1yabw_ydLR"
GIT_PATH=$GIT_LOGIN

GIT_DIR="/home/$USER/$URL"
PROD_DIR="/var/www/$URL"

VENV_BIN="$PROD_DIR/.venv/bin"
ACTIVATE="source $VENV_BIN/activate"
MANAGE="$VENV_BIN/python $PROD_DIR/$PROJECT/manage.py"
DJANGO_SETTINGS_MODULE="$PROJECT.settings.production"

echo "-----------------"
date

echo ""
echo "+ Pulling newest commit."
git pull https://$GIT_LOGIN:$GIT_PASS@gitlab.com/$GIT_PATH/$URL.git

echo ""
echo "+ Updating supervisor + nginx config files."
sudo cp $GIT_DIR/$PROJECT/$PROJECT/settings/supervisor/aynurotyakmaz-com.conf /etc/supervisor/conf.d/aynurotyakmaz-com.conf
sudo cp $GIT_DIR/$PROJECT/$PROJECT/settings/nginx/aynurotyakmaz-com.conf /etc/nginx/conf.d/aynurotyakmaz-com.conf

echo ""
echo "+ Copy files to /var/www"
sudo cp -a $GIT_DIR/. $PROD_DIR

if [ ! -d $VENV_BIN ]; then
  echo ""
  echo "+ Creating virtual environment."
  virtualenv -p python3 $PROD_DIR/.venv
fi

if [ ! -d $PROD_DIR/logs ]; then
  echo ""
  echo "+ Creating log directory."
  sudo mkdir $PROD_DIR/logs
fi

echo ""
echo "+ Updating permissions."
sudo chown -R dylan:www-data $PROD_DIR
sudo chmod -R 0755 $PROD_DIR

echo ""
echo "+ Installing dependencies."
$VENV_BIN/pip install -r $PROD_DIR/$PROJECT/requirements.txt

last_line=$(tail -1 $VENV_BIN/activate)
if [ last_line != "DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE" ]; then
  echo ""
  echo "+ Modifying virtual environment for production."
  echo "export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE" >> $VENV_BIN/activate
fi

echo ""
echo "+ Making migrations and collecting static + updating permissions again."
$ACTIVATE
$MANAGE makemigrations
$MANAGE migrate
$MANAGE collectstatic --noinput
sudo chown -R dylan:www-data $PROD_DIR
sudo chmod -R 0755 $PROD_DIR

echo ""
echo "+ Restarting supervisor + nginx."
sudo supervisorctl update $PROJECT
sudo supervisorctl restart $PROJECT
sudo service nginx restart

echo ""
echo "+ Finished."
echo "---------------"
