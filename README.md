Project setup

    1. create kudago/local_settings.py file with your database settings
    2. create database and user in psql according on your local_settings
    3. virtualenv -p python3 venv
    4. source venv/bin/activate
    5. pip install -r requirements.txt
    6. ./manage.py migrate

Load xml feed

    ./manage.py loadxml `source_file`
