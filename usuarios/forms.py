from django import  forms
from .models import ONG, Administrador, Voluntario

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = "__all__"
class ONGForm(forms.ModelForm):
    class Meta:
        model = ONG
        fields = "__all__"
class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = "__all__"




