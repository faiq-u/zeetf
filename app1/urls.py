from django.urls import path
from . import views
from .models import thoughts

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index')
]
iterable = thoughts.objects.all()
for person in iterable:
    x = path(str(person.Pers_name),views.comment,name=str(person.Pers_name))
    urlpatterns.append(x)