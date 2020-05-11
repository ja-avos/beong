from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VoluntarioForm,Voluntariologin
from django.contrib import messages
from django.urls import  reverse
from .models import Voluntario
from .models import ONG
from voluntariados import services

def voluntario_create(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["usuario"]
            voluntario = form.save()
            voluntario.save()
            user = Voluntario.objects.get(usuario = user)
            context ={
                "user":user
            }
            messages.add_message(request, messages.SUCCESS, 'Voluntario satisfactoriamente creado')
            return render(request, 'index.html', context)
        else:
            print(form.errors)
    else:
        form = VoluntarioForm()

    context = {
        "user":None,
        'form': form,
    }
    return render(request, 'usuarios/register.html', context)
def generate_login(request):
    if request.method == 'POST':
        form = Voluntariologin(request.POST)
        if form.is_valid():
            isONG = form.cleaned_data.get("ong")
            usuario = form.cleaned_data.get("usuario")
            password = form.cleaned_data.get("password")
            if isONG:
                try:
                    ong =  ONG.objects.get(usuario = usuario)
                    if ong != None:
                        if ong.contrasenia == password:
                            context ={
                                "user": ong
                            }
                            return render(request, "index.html", context)
                    else:
                        messages.add_message(request, messages.ERROR, "Contraseña incorrecta")
                except:
                    messages.add_message(request, messages.ERROR, "No existe una ONG con ese usuario")

            else:
                try:
                    user =  Voluntario.objects.get(usuario = usuario)
                    if user != None:
                        if user.contrasenia == password:
                            context ={
                                "user": user
                            }
                            return render(request, "index.html", context)
                    else:
                        messages.add_message(request, messages.ERROR, "Contraseña incorrecta")
                except:
                    messages.add_message(request, messages.ERROR, "No esxiste un voluntario con ese usuario")


            messages.add_message(request, messages.SUCCESS, 'Voluntariado logeado correctamente"')
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = Voluntariologin()
    context = {
        "user":None,
        'form': form,
    }
    return render(request, "usuarios/login.html", context)


def generate_detail(request, username):
    user = Voluntario.objects.get(usuario = username)
    active = services.getActiveProcesses(user)
    print(active)
    recommend = services.getRecVolunteers(user)
    liked = services.getLikedVolunteers(user)
    context = {
        "user":user,
        "active": active,
        "recommend": recommend,
        "liked": liked
    }
    return render(request,"usuarios/detail.html",context)


# Create your views here.
