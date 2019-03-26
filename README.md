## django project titled mark-dojo ##

#### Conception: 03/23/2019


### Getting comfortable

pip3 install pipenv

mkdir markdojo; cd markdojo

pipenv install django==2.1

pipenv shell

django-admin startproject markdojo_project .


#### Create an app under markdojo_project

python manage.py startapp hello

subl .

** edit files: 
	markdojo_project/settings.py, 
	markdojo_project/urls.py, 
	hello/views.py

### Create a to-do app

python manage.py startapp todo

### models -- database integration

python manage.py makemigrations

python manage.py migration


### Run server

python manage.py runserver
