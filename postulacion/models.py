from django.db import models
from voluntariados.models import Voluntariado


class Postulacion(models.Model):
    fecha= models.DateField()
    estado=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True)
    voluntariado=models.ForeignKey(Voluntariado, on_delete=None)

# Create your models here.
