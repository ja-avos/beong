from django.shortcuts import render
from .models import Voluntariado
from django.http import JsonResponse

def getVoluntariados(request):
    volunteers = Voluntariado.objects.all()
    return JsonResponse(volunteers)

def index(request):
    latest_volunteers = Voluntariado.objects.order_by('nombre')
    context = {'latest_volunteers': latest_volunteers}
    return render(request, 'voluntariados/voluntariados.html', context)

# Create your views here.
