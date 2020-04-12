from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addPerson, name='addPerson'),
    path("usuarios/", include("usuarios.urls")),
    path('acerca', views.about, name='about'),
    path('add', views.addPerson, name='addPerson')

]