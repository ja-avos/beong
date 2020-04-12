from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca', views.about, name='about'),
    path('add', views.addPerson, name='addPerson')
]