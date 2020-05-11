from usuarios.models import Voluntario, ONG
from voluntariados.models import Voluntariado
from postulacion.models import Postulacion

from beong.settings import EMAIL_HOST_USER, BASE_DIR
from django.core.mail import send_mail
from django.template import loader

from clasifiacion import clasificar

from datetime import date

def getLikedVolunteers(volunteer: Voluntario):
    vols = []
    for i in Postulacion.objects.filter(voluntario = volunteer.usuario):
        if i.getHistorial().count(Postulacion.INTERESTED) > i.getHistorial().count(Postulacion.NOTINTERESTED):
            prik = i.voluntariado
            vols.append(prik)
    return vols

def apply(user: Voluntario, vol: Voluntariado):
    changed = False
    try:
        postulacion = Postulacion.objects.get(voluntariado=vol.id, voluntario=user.usuario)
        if postulacion.estado == Postulacion.INTERESTED:
            postulacion.estado = Postulacion.APPLIED
            historial = postulacion.getHistorial()
            historial.append(Postulacion.APPLIED)
            postulacion.setHistorial(historial)
            postulacion.save()
            changed = True
    except Postulacion.DoesNotExist:
        postulacion = Postulacion(estado = Postulacion.INTERESTED, voluntariado = vol, voluntario = user)
        postulacion.setHistorial([Postulacion.APPLIED])
        postulacion.save()
        changed = True
    if changed:
        correo = user.correo
        volun = vol.nombre
        send_email(correo, 'Aplicación Exitosa ' + date.today().strftime("%d-%m-%y"), "Aplicación",
                       loader.render_to_string('mail/apply_mail.html', {'voluntariado': volun}))
        send_email('gd.martinez@beong.me', 'Aplicación Exitosa ' + date.today().strftime("%d-%m-%y"), "Aplicación",
                       loader.render_to_string('mail/apply_mail.html', {'voluntariado': volun}))
    return changed

def likeVolunteer(user: Voluntario, vol: Voluntariado):
    try:
        postulacion = Postulacion.objects.get(voluntariado=vol.id, voluntario=user.usuario)
        if postulacion.getHistorial().count(Postulacion.INTERESTED) <= postulacion.getHistorial().count(Postulacion.NOTINTERESTED):
            postulacion.estado = Postulacion.INTERESTED
            historial = postulacion.getHistorial()
            historial.append(Postulacion.INTERESTED)
            postulacion.setHistorial(historial)
            postulacion.save()
    except Postulacion.DoesNotExist:
        postulacion = Postulacion(estado = Postulacion.INTERESTED, voluntariado = vol, voluntario = user)
        postulacion.setHistorial([Postulacion.INTERESTED])
        postulacion.save()
    except Postulacion.MultipleObjectsReturned:
        #TODO Pasa
        return
    print(postulacion)

def dislike(user: Voluntario, vol: Voluntariado):
    try:
        postulacion = Postulacion.objects.get(voluntariado=vol.id, voluntario=user.usuario)
        if postulacion.getHistorial().count(Postulacion.INTERESTED) > postulacion.getHistorial().count(Postulacion.NOTINTERESTED):
            postulacion.estado = Postulacion.NOTINTERESTED
            historial = postulacion.getHistorial()
            historial.append(Postulacion.NOTINTERESTED)
            postulacion.setHistorial(historial)
            postulacion.save()
    except Postulacion.DoesNotExist:
        return 
    except Postulacion.MultipleObjectsReturned:
        #TODO Pasa
        return

def getOrgVoluntariados(ong: ONG):
    return Voluntariado.objects.filter(organizacion = ong.usuario)

def getActiveProcesses(user: Voluntario):
    process = Postulacion.objects.filter(voluntario = user.usuario)
    active = []
    for j in process:
        historial = j.getHistorial()
        historial = [i for i in historial if i != Postulacion.INTERESTED and i != Postulacion.NOTINTERESTED]
        if len(historial) - 1 < 0:
            continue
        if j.estado == Postulacion.INTERESTED or j.estado == Postulacion.NOTINTERESTED:
            j.estado = historial[len(historial)-1]
        if Postulacion.CANCELLED not in historial and historial[len(historial)-1] != Postulacion.INTERESTED and historial[len(historial)-1] != Postulacion.NOTINTERESTED:
            active.append(j)
    return active

def getRecVolunteers(user: Voluntario):
    lista = clasificar.getVoluntariados(user.usuario)
    lisres = []
    tmp = [i[0] for i in lista if len(i) == 1]
    for n in tmp:
        lisres.append(Voluntariado.objects.get(id=n[0]))
    return lisres

def send_email(dest_mail, subject, content, html):
    send_mail(subject, content, 'BeONG <support@beong.me>', [dest_mail], html_message=html)