from django.shortcuts import render
from .models import Voluntariado
from django.http import JsonResponse
from .logic_voluntariado.logic_voluntariado import create_Voluntariado
from django.urls import reverse
from .forms import VoluntariadoForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def getVoluntariados(request):
    volunteers = Voluntariado.objects.all()
    return JsonResponse(volunteers)

def index(request):
    latest_volunteers = Voluntariado.objects.order_by('nombre')
    context = {'latest_volunteers': latest_volunteers}
    return render(request, 'voluntariados/voluntariados.html', context)

def createVoluntariado(request):
    if request.method == 'POST':
        form = VoluntariadoForm(request.POST)
        if form.is_valid():
            create_Voluntariado(form)
            messages.add_message(request, messages.SUCCESS, 'Voluntariado satisfactoriamente creado')
            return HttpResponseRedirect(reverse('createVoluntariado'))
        else:
            print(form.errors)
    else:
        form = VoluntariadoForm()

    context = {
        'form': form,
    }
    return render(request, 'Voluntariados/create.html', context)

# Create your views here.
