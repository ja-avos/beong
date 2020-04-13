from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='voluntariados'), #Falta hacerla
    path('list', views.getVoluntariados, name='getVoluntariados')
]