from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from .models import Person
import json

def index(request):
    return render(request, 'landing/index.html')

def about(request):
    return render(request, 'landing/about.html')

def experiences(request):
    return render(request, 'landing/experiences.html')

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
