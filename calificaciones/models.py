from django.db import models

class Calificacion (models.Model):
    puntuacion=models.IntegerField()
    comentario=models.CharField(max_length=100)
    nombreVoluntario= models.CharField(max_length=50)

# Create your models here.
