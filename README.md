Project setup

    1. create kudago/local_settings.py file with your database settings
       or take a look kudago/settings.py
    3. virtualenv -p python3 venv
    4. source venv/bin/activate
    5. pip install -r requirements.txt
    6. ./manage.py migrate

Load test.xml feed

    ./manage.py loadxml feed/test.xml
