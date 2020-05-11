
from django.shortcuts import render
from .models import Voluntariado
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from beong.settings import EMAIL_HOST_USER, BASE_DIR
from django.core.mail import send_mail
from django.template import loader
import os
import json
from .logic_voluntariado.logic_voluntariado import create_Voluntariado
from django.urls import reverse
from .forms import VoluntariadoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
import datetime
import sys
sys.path.append("..")
from usuarios.models import  Voluntario,ONG

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
    context = {'latest_volunteers': latest_volunteers,
               'areas': areas,
               'locations': locations,
               "user":user,
               }
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
    #if filters['duramin'] != '' or filters['duramax'] != '':
    #    volsd = []
    #    for v in vols:
    #        durS = v.duracion
    #        if filters['duramin'] != '' and filters['duramax'] == '' and convertDuration(durS) >= convertDuration(
    #                filters['duramin']):
    #            volsd.append(v)
    #        elif filters['duramin'] == '' and filters['duramax'] != '' and convertDuration(durS) <= convertDuration(
    #                filters['duramax']):
    #            volsd.append(v)
    #        elif filters['duramin'] != '' and filters['duramax'] != '' and convertDuration(durS) >= convertDuration(
    #                filters['duramin']) and convertDuration(durS) <= convertDuration(filters['duramax']):
    #            volsd.append(v)
    #    return volsd
    return vols


def save_volunteer(request):
    # TODO Save volunteer to user wishlist
    return request


@csrf_exempt
def apply_volunteer(request,username):
    user = None
    if username != "Visitante":
        Usuario = Voluntario.objects.get(usuario = username)
        correo = Usuario.correo
        # TODO Apply to specified volunteer
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            send_email(correo, 'Aplicación Exitosa' + body['saludo'], "Aplicación",
                       loader.render_to_string('mail/apply_mail.html', {'voluntariado': 'Prueba'}))
            send_email('gd.martinez@beong.me', 'Aplicación Exitosa' + body['saludo'], "Aplicación",
                       loader.render_to_string('mail/apply_mail.html', {'voluntariado': 'Prueba'}))
        return HttpResponse('Good')





def send_email(dest_mail, subject, content, html):
    send_mail(subject, content, 'BeONG <support@beong.me>', [dest_mail], html_message=html)


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

# Create your views here.
