from django.db import models
from intereses.models import Gusto, Idioma
from calificaciones.models import Calificacion

class Voluntariado (models.Model):
    nombre = models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)
    area=models.CharField(max_length=20)
    duracion=models.CharField(max_length=20)
    lugar=models.CharField(max_length=25)
    precio=models.FloatField()
    requsitos=models.CharField(max_length=50)
    gustosRequeridos=models.ForeignKey(Gusto, on_delete=None)
    idiomasRequeridos=models.ForeignKey(Idioma, on_delete=None)
    calificaciones=models.ForeignKey(Calificacion, on_delete=models.CASCADE)

