from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VoluntarioForm
from django.contrib import messages
from django.urls import  reverse
from .models import Voluntario

def voluntario_create(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            voluntario = form.save()
            voluntario.save()
            messages.add_message(request, messages.SUCCESS, 'Voluntario satisfactoriamente creado')
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = VoluntarioForm()

    context = {
        'form': form,
    }
    return render(request, 'usuarios/register.html', context)





# Create your views here.
