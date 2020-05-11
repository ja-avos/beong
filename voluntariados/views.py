
from django.shortcuts import render
from .models import Voluntariado
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import os
import json
from .logic_voluntariado.logic_voluntariado import create_Voluntariado
from django.urls import reverse
from .forms import VoluntariadoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
import datetime
from usuarios.models import  Voluntario,ONG
from voluntariados import services

def getVoluntariados(request):
    volunteers = Voluntariado.objects.all()
    return JsonResponse(volunteers)


def index(request, username):
    user = None
    if username != "Visitante":
        try:
            user = Voluntario.objects.get(usuario=username)
        except:
            user = ONG.objects.get(usuario=username)
    latest_volunteers = Voluntariado.objects.order_by('nombre')
    areas = set([])
    locations = set([])
    for v in latest_volunteers:
        areas.add(v.area)
        locations.add(v.lugar)
    filters = {}
    filters['name'] = request.GET.get('name', '')
    filters['area'] = request.GET.get('area', '')
    filters['location'] = request.GET.get('location', '')
    filters['pricemin'] = request.GET.get('pricemin', '')
    filters['pricemax'] = request.GET.get('pricemax', '')
    filters['duramin'] = request.GET.get('duramin', '')
    filters['duramax'] = request.GET.get('duramax', '')

    latest_volunteers = filter_vol(latest_volunteers, filters)
    liked_vols = []
    if username != 'Visitante':
        liked_vols = services.getLikedVolunteers(user)
    context = {'latest_volunteers': latest_volunteers,
               'liked_vols': liked_vols,
               'areas': areas,
               'locations': locations,
               "user":user,
               }
    print(services.getLikedVolunteers(Voluntario.objects.get(usuario = username)))
    return render(request, 'voluntariados/voluntariados.html', context)


def filter_vol(vols, filters):
    def convertDuration(durS):
        durS = durS.lower()
        dur = -1 if durS == '' else 0
        if 'mes' in durS:
            dur += int(durS.split('mes')[0].strip()) * 30
        elif 'semana' in durS and not 'fin de semana' in durS:
            dur += int(durS.split('semana')[0].strip()) * 7
        elif 'dia' in durS:
            dur += int(durS.split('dia')[0].strip())
        elif 'día' in durS:
            dur += int(durS.split('día')[0].strip())
        elif 'año' in durS:
            dur += int(durS.split('año')[0].strip()) * 365
        elif 'anio' in durS:
            dur += int(durS.split('anio')[0].strip()) * 365
        return dur

    vols = vols.filter(nombre__icontains=filters['name'])
    if filters['area'] != '':
        vols = vols.filter(area__exact=filters['area'])
    if filters['location'] != '':
        vols = vols.filter(lugar__exact=filters['location'])
    if filters['pricemin'] != '':
        vols = vols.filter(precio__gte=int(filters['pricemin']))
    if filters['pricemax'] != '':
        vols = vols.filter(precio__lte=int(filters['pricemax']))
    if filters['duramin'] != '':
        vols = vols.filter(duracion__gte=int(filters['duramin']))
    if filters['duramax'] != '':
        vols = vols.filter(duracion__lte=int(filters['duramax']))
    return vols

@csrf_exempt
def save_volunteer(request, username):
    user = None
    if username != "Visitante":
        usuario = Voluntario.objects.get(usuario = username)
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            vol = Voluntariado.objects.get(id = int(body['vol_id']))
            services.likeVolunteer(usuario, vol)
    return HttpResponse('Good')

@csrf_exempt
def dislike_volunteer(request, username):
    user = None
    if username != "Visitante":
        usuario = Voluntario.objects.get(usuario = username)
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            vol = Voluntariado.objects.get(id = int(body['vol_id']))
            services.dislike(usuario, vol)
    return HttpResponse('Good')

@csrf_exempt
def apply_volunteer(request,username):
    user = None
    if username != "Visitante":
        user = Voluntario.objects.get(usuario = username)
        # TODO Apply to specified volunteer
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            voluntariado = Voluntariado.objects.get(id = int(body["id"]))
            services.apply(user, voluntariado)
        return HttpResponse('Good')


def createVoluntariado(request,username):
    user = None
    if username != "Visitante":
        try:
            user = ONG.objects.get(usuario=username)
        except:
            user = ONG.objects.get(usuario=username)
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
        "user": user,
        'form': form,
    }
    return render(request, 'voluntariados/create.html', context)
