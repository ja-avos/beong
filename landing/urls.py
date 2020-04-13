from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca', views.about, name='about'),
    path('experiencias', views.experiences, name='experiences'),
    path('add', views.addPerson, name='addPerson')
]