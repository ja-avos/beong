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
        required_css_class = 'bold'
        fields = (
            "nombre",
            "usuario",
            "contrasenia",
            "descripcion",
            "edad",
            "pais",
            "ciudad",
            "departamento",
            "ocupacion",
            "idiomas",
            "gustos",
            "correo",
        )
        widgets = {
            "nombre":forms.TextInput(attrs= {"placeholder": "Tu nombre"}),
            "usuario":forms.TextInput(attrs = { "placeholder": "Usuario cool"}),
            "contrasenia":forms.PasswordInput(),
            "descripcion":forms.Textarea(attrs = {"placeholder":"¡Cuéntamos lo mejor de ti!"}),
            "pais":forms.TextInput(attrs = {"placeholder": "País donde vives"}),
            "ocupacion":forms.TextInput(attrs = { "placeholder":"Cuéntanos a qué te dedicas"}),
            "ciudad":forms.TextInput(attrs = {"placeholder": "Ciudad"}),
            "departamento":forms.TextInput(attrs={"placeholder":"Departamento"}),
        }
        labels = {
            "nombre" : "Nombre",
            "usuario": "Usuario",
            "contrasenia": "Contraseña",
            "descripcion": "Descripción",
            "edad": "Edad",
            "pais": "País",
            "ocupacion": "Ocupacion",
            "idiomas": "Idiomas",
            "ciudad":"Ciudad",
            "departamento":"Departamento",
            "gustos":"Gustos",
            "correo":"Correo",
        }
class Voluntariologin(forms.Form):
    usuario = forms.CharField(label = "Usuario")
    password = forms.CharField(widget=forms.PasswordInput())








