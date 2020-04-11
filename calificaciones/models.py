from django.db import models
class Califiacion (models.Model):
    id=models.IntegerField(primary_key=True)
    puntuacion=models.IntegerField()
    comentario=models.CharField(max_length=100)

# Create your models here.
