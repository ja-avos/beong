from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from .models import Person
import sys
sys.path.append("..")
from usuarios.models import  Voluntario, ONG

import json

def index(request):
    context = {
        "user":None

    }
    return render(request, 'landing/index.html', context)

def about(request, username):
    user = None
    if username != "Visitante":
        try:
            user = Voluntario.objects.get(usuario = username)
        except:
            user = ONG.objects.get(usuario = username)
    context = {
        "user":user
    }

    return render(request, 'landing/about.html',context)

def experiences(request, username ):
    user = None
    if username != "Visitante":
        try:
            user = Voluntario.objects.get(usuario=username)
        except:
            user = ONG.objects.get(usuario=username)
    context = {
        "user":user
    }
    return render(request, 'landing/experiences.html', context)

@csrf_exempt
def addPerson(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        emailR = body["email"]
        try:
            person = Person(email=emailR)
            person.save()
        except Exception as e:
            return HttpResponseServerError('No se pudo registrar :(' + str(e))
        return HttpResponse("OK")
    return HttpResponseBadRequest('Bad request')
        

# Create your views here.
