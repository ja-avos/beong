from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addPerson, name='addPerson'),
    path('acerca/<str:username>', views.about, name='about'),
    path('experiencias/<str:username>', views.experiences, name='experiences'),
    path('add', views.addPerson, name='addPerson')

]