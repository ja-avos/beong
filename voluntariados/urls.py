from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='voluntariados'),
    path('list', views.getVoluntariados, name='getVoluntariados'),
    path('apply', views.apply_volunteer, name='apply'),
    path('create',views.createVoluntariado,name='createVoluntariado')
]