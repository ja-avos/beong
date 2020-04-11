from django.db import models

class Calificacion (models.Model):
    id=models.IntegerField(primary_key=True)
    puntuacion=models.IntegerField()
    comentario=models.CharField(max_length=100)
    nombreVoluntario= models.CharField(max_length=50)

# Create your models here.
