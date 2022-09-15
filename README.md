# Django Project

A simple Django project to display artist name and description.

### setup 
- `pip install pipenv `
- `pipenv shell `
- `pipenv install django`
- `django-admin startproject songs` (name of project = songs)

### Run server: 
- cd into shelter 
- `python manage.py runserver` --> localhost 8000

### PROJECT APP: 
- `python manage.py startapp artists`
- add .gitignore 
- connect app to project: settings.py add to INSTALLED_APPS name of app(artists)
- urls.py add path(artists) and import include 

- create usrls.py in artists(app name) folder and add stuff inside 
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="artists-home")
]
```
- add to views in artists stuff
- `python manage.py runserver` see server 8000/artists 

- add contact/ path in views
- add stuff to views.py (contact) check 8000/artists/contact

- show path by id ,songs
- see `http://localhost:8000/artists/songs and http://localhost:8000/adoption/dogs/1`

### templates
- create templates folder /artists/base.html in artists 
- connect templates to views.py:
 -  use `render` and change all functions in views.py and add all html files in artists next to templates (home,contact,show,artist)
 - `home.html` add block and content
 - same with contact and the rest



# DATABASE

- add stuff to models.py
- `python manage.py makemigrations artists`  (models.py converted to sth understandable)
- `python manage.py migrate` run migration
- `python manage.py createsuperuser` chess@exampl.com playchess123  --> Created user in DJANGO
- `python manage.py runserver` Go to 8000/admin -> login
- admin.py in artists --> add stuff to populate database


- add artists genre type- save
- create artists - save 
- see list 

- GOAL: we want read db :
- views.py `from .models import Artist`
- change functions

- add 404 and 500 and create files in templates htmls
- add to urls in songs!!
``
handler404 = 'artists.views.not_found_404'
handler500 = 'artists.views.server_error_500'
``
- change setting in setting.py:
    - True to False
    - `ALLOWED_HOSTS = ['localhost', '127.0.0.1']`
- re-run server: `python manage.py runserver`
- start on different port `python manage.py runserver 4000`

[Link to tests](https://djangostars.com/blog/django-pytest-testing/)