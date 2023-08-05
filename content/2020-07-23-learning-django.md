---
title: "Learning Django"
date: "2020-07-23"
tags: ["Developer"]
image: "https://www.dropbox.com/s/gxx3ii5817i3jez/django.png?raw=1"
gradients: ["#314755", "#314755"]
---

## Abstraction
This is a minor guide and note that are used to start a Django project. The post will be short because, it basically, just the setup of Django. I’ll be relating it Flask as well, its simpler for me to understand, as I know Flask.

## Installing Django
Note that is might good to setup a **venv**.

```py
pip3 install django

# List of commands
djano admin

# Starting new Project
django-admin startproject django_project_name
cd django_project_name

# Run server, usually python3 app.py in Flask
python3 manage.py runserver

# Start app, creating like component section for app.
python3 manage.py startapp name_of_app
# Creates a name_of_app folder
# Contain views.py which
```

### Setup up url path and function.
The most important files in `name_of_app` is the `views.py` and `url.py`. In Flask this can be in file called `routes.py`. Instead of something like,

```py
@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template(index.html)
```

where the path and function is together, Django splits it up into two files like the following below.

```py
# In views.py add,
from djano.http import HttpReponse

# This is all , where the urls will access, when they match the path of url.
def home(request):
	return HttpResponse(index.html)

# =================================================

# Create urls.py in name_of_app and add,
from django.contrib import admin
from django.url import path, includes
from . import views

urlpatterns = [
	path('', views.home, name='home-blog') # Maps from views.py home func
]
```

You also need to make sure that you setup urlpath in the `src/urls.py folder`.

```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('name_of_app.urls')),
]
```
That why, in root, it can make paths to your app, and in the app it will make paths to you `views.py`.

### Using /admin to create db models
One thing I like about Django, is creating a model for a db very easy, and Django is able to store instances created in the `/admin` section. You can also manage these instances, such as edit and deleting them. Assuming you have created a model in `models.py`, like so

```py
from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)      # requirements: max_length=int
    topic = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
```
To add it in Django, and to manage it, you need to create a superuser and migrate.

```py
# This is for when updating or adding a model in Django
# update db
python3 manage.py makemigrations

# create authuser
python3 manage.py migrate

# To manage models and default users, create a superuser
# create superuser requires authuser from db
python manage.py createsuperuser
# Now you can goto localhost:port/admin and you can manage user and groups and created model.
```

## First Impression
There was more I’ve learnt that I didn’t bother writing down, as I felt like I can remember them, but this is the basics to getting things working. These rest, such as html templating is basically the same as Flask and Jinja. That said, Django I think is a much complex framework, but not difficult to understand, it in my opinion has better functionalities than Flask, as Flask is basic and simply. Things like managing users and security, is a massive improve in Django. Overall, I feel like Django is very good for creating a full scale backend application, where as Flask, is useful for prototyping and making Restful APIs.