from django.db import models
from intereses.models import Gusto, Idioma
from calificaciones.models import Calificacion

class Voluntariado (models.Model):
    nombre = models.CharField(max_length=50)
    area=models.CharField(max_length=20)
    duracion=models.CharField(max_length=30)
   # descripcion=models.CharField(max_length=200)
    lugar=models.CharField(max_length=25)
    precio=models.FloatField()
    gustosRequeridos=models.ManyToManyField(Gusto)
    idiomasRequeridos=models.ManyToManyField(Idioma)
    calificaciones=models.ManyToManyField(Calificacion, blank=True)

    def __str__(self):
        return '%s' % (self.nombre)

