from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("register/", csrf_exempt(views.voluntario_create), name = "voluntarioRegister"),
    path("login/", csrf_exempt(views.generate_login), name = "voluntarioLogin"),
    path("detail/<str:username>", csrf_exempt(views.generate_detail), name = "voluntariodetail"),
]