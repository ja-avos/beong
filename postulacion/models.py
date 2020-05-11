from django.db import models
from django.utils import timezone
from voluntariados.models import Voluntariado
from usuarios.models import Voluntario
import json
import datetime


class Postulacion(models.Model):
    INTERESTED = 'INTERESTED'
    APPLIED = 'APPLIED'
    REVISION = 'REVISION'
    ACCEPTED = 'ACCEPTED'
    PAYSUC = 'PAYSUC'
    ONVOL = 'ONVOL'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'
    NOTINTERESTED = 'NOTINTERESTED'

    fecha= models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20)
    historial = models.CharField(max_length=200, default='{}')
    voluntariado=models.ForeignKey(Voluntariado, on_delete=models.CASCADE, default = None)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, default = None)

    def setHistorial(self, x):
        self.historial = json.dumps(x)

    def getHistorial(self):
        return json.loads(self.historial)


# Create your models here.
