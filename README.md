# Proth project
**Your personal tool to stay highly productive and smart!**

Here you can keep your personal goals, track your updates, plan your time and learn new languages!
## Pre-conditions for installation
```
1. Python 3.8.10
2. Git
3. PostgreSQL on machine
4. pyenv/standart python tool for creating virtual environments.
5. .env file with django secret-key. 
```
## How to install?
```
1. git clone git@github.com:itsdaibend/proth.git
2. Move .env file to core django-app folder.
3. pyenv virtualenv 3.8.10 proth
4. pyenv activate proth
5. pip install -r requirements.txt
6. psql
7. CREATE DATABASE proth;
8. python manage.py migrate
9. python manage.py createsuperuser
10. python manage.py runserver
```
## How to run?
```
1. source env_name/bin/activate OR pyenv activate proth
2. sudo service postgresql start
3. cd django_app
4. python manage.py runserver
```
