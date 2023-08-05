---
title: "Learning Django Rest Framework"
date: "2022-02-26"
tags: ["Web", "Developer", "API"]
image: ""
gradients: ["#085078", "#085078"]
---
         
### Motivation
Yes, back into Python, I did Django a few year back but this time it's creating and *REST api* with Django REST framework. This post will be more of a extenstion to that Django post. I need to learn this for a project I'm getting involved in. But before I start I want to note down some important features in Django.

### Signals [Doc](https://docs.djangoproject.com/en/4.0/topics/signals/).
Everytime a model is defined, we can have a **signal** that handles the model in some way. Most of the time, there signals are written in the `models.py`

The following are two equivalent code,
```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ModelClass  # not neccasary if you are adding signals in the models.py

@receiver(pre_save, sender=ModelClass) # Option 1
def callback(*args, **kwargs):
    print("Request finished!")

pre_save.connect(callback, sender=ModelClass) # Option 2
```

The code above, whether using option 1 or 2, tells us that onces a `ModelClass` (usually in `models.py`) is *save*, as in somewhere in Django, `ModelClass.save()` then this callback will be prompted.

So there are other methods other than `pre_save` such as,
- `pre_save`
- `post_save` - called **before** the instance is *saved* in the database
- `pre_delete`
- `post_delete`

Note a important to **avoid** is adding `ModelClass.save()`, `ModelClass.delete()` etc in the *pre* callback signals as that will trigger the *trigger* the signal recursive and screw the stack over.

A useful real application can be with the *deletes* signals, such when a user deletes an instance of the model, the `pre_delete` can capture that can the application can have something that caches the deleted instance, for a period of time, before permenantly deleting it. That way, if the user was to restore the instance, they can.

### QuerySet [Doc](https://docs.djangoproject.com/en/4.0/ref/models/querysets/)
This is fairly simple, again mostly done in `models.py`. It is more of a API for the Django `model` and makes it easier for querying data. Stuff like,
- `model.objects.all()`
- `model.objects.filter()`
- `model.objects.orderby()`
- `model.objects.count()` - the same as `len()` but more efficient
There are many more that can be found in the doc.

### Templates
Templates for Django are essentially an engine that is used for **dynamic render** our data in html. This can be things from creating layouts to avoid duplicate html codes or using python sytnax for display backend data.

The main sytnax Django template use is,
```html
{{ include 'navbar.html' }}

{% for item in items %}
    <div>
        <a href="{{ url 'item.url' item.id }}">
            {{ i.title }}
        </a>
    </div>
{% end for %}
```

A simple example is the one above where this `.html` will first include the navbar *component* where ever `navbar.html` is stored. Then the templates allow us to use python sytnax such as `if` or `for` to loop through our `context` param passed in the backend. In this case, the backend as passed context like this,
```py
context = {
    "item": items # where items can be a list of class that will contain attributes like url, id and title to show in the template engine
}
```

#### Slug
This is a personal note of the use `slug()`. This can be defined as a *type* in the model classes, denoted as, 
```py
title = models.TextField()
slug = models.SlugField()
```
The purpose of this is to **generate a valid url** format. An example using `title` which can be a string like,
```py
title = "A Valid Url Example"
slug = slug(title) # a-valid-url-example
```

### Django Rest framework
At this point, a project with a backend and modelled class should have been programmed, with the templating engine to help assist with the UI of CRUD the data. Now we want to make use of an API to share the data for other applications, etc. 

#### Installation
```
pip install djangorestframework
```

and in `settings.py`, 
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

#### Connecting our REST api endpoints to Django application
In our main project, we will need to add our api urls to the main urls
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('main.api.urls'))  # Add here
]
```
This way, our all our normal Django application urls will be access with beginning with `/` and all the apis endpoints will be access beginning with `/api`.

#### Creating an endpoint

In our `views.py` and `urls.py` this is essentially similar to as the backend application. Let first take a look at `urls.py`
```py
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.get_routes),
    path('plan/', views.get_plans),
    path('plan/<int:pk>/', views.get_plan),
]
```

Hence for all the urls paths here, since will specified that the api urls will begin with `api`, the urlpattern for `plan/` with be `/api/plan`,

Now time for the implementation of the these endpoints, this will also be implementating the **serializer** that is required to change the our model classes to json format for display toour endpoints. For now the code below is a simply version of an endpoint.

```py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/plan',
        'GET /api/plan/:id'
    ]
    return Response(routes)
```

where we import from the `rest_framework` the `api_view` to specific our http method and `Response` to send a JSON format data. Now instead, we want to send back the ModelClass as data, we can't because the class isn't going to tranform itself to JSON for us, so instead we need a *serializerModel* that does. This is typically done in the `serializers.py`.

```py
from rest_framework.serializers import ModelSerializer
from base.models import ModelClass

class ModelClassSerializer(ModelSerializer):
    class Meta:
        model = ModelClass
        fields = '__all__'
```

A basic serialisation of a Model is like so. Very simple and self explanatory. Loading in the framework Class, using it as a parent class and mapping it to our ModelClass.

Coming back to the `views.py` now, we can query our ModelClass by importing both the *model* and the *serialiser* and following the format below,
```py
from main.models import ModeClass
from .serializers import ModeClassSerializer

@api_view(['GET'])
def get_plans(request):
    plans = ModeClass.objects.all()
    serializers = ModeClassSerializer(plans, many=True)
    return Response(serializers.data)
```

Some things to note are,
- Ensure that when we call our serialiser that if there are **more than one** objects return to use flag, `many=True`. For only one object, this is not required.
- The acutally data in json is in `serialisers.data`. That is the raw JSON object is in the `data` key. 

### Conclusion
That is all for creating a simple endpoint that utilises the Django model classes.