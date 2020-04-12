from django.contrib import admin
from .models import ONG, Administrador, Voluntario

# Register your models here.
admin.site.register(Voluntario)
admin.site.register(ONG)
admin.site.register(Administrador)