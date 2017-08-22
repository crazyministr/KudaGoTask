Project setup
    create kudago/local_settings.py file with your database settings
    create database and user in psql according on your local_settings
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate

Load xml feed
    ./manage.py loadxml `source_file`
