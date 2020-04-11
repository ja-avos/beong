from django.db import models

class Voluntariado (models.Model):
    nombre = models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)
    area=models.CharField(max_length=20)
    duracion=models.CharField(max_length=20)
    lugar=models.CharField(max_length=25)
    precio=models.FloatField()
    requsitos=models.CharField(max_length=50)
# Create your models here.
