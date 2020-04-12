from django.db import models
from voluntariados.models import Voluntariado


class Postulacion(models.Model):
    fecha= models.DateField()
    estado=models.CharField(max_length=20)
    voluntariado=models.ForeignKey(Voluntariado, models.SET_NULL, null=True,)



# Create your models here.
