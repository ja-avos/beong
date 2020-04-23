from django import forms
from .models import Voluntariado

class VoluntariadoForm(forms.ModelForm):
    class Meta:
        model = Voluntariado
        fields = [
            'nombre',
            'area',
            'duracion',
            'descripcion',
            'lugar',
            'precio',
            'gustosRequeridos',
            'idiomasRequeridos',
            'imagen',
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Ingresa el nombre de tu voluntariado"}),
            "area": forms.TextInput(attrs={"placeholder": "Ingresa el area de tu voluntariado"}),
            "duracion": forms.TextInput(attrs={"placeholder": "Ingresa la duración de tu voluntariado"}),
            "descripcion": forms.Textarea(attrs={"placeholder": "Ingresa una descripción de tu voluntariado",
                                                 "rows":4, "cols":50}),
            "lugar": forms.TextInput(attrs={"placeholder": "Ingresa el lugar de tu voluntariado"}),
            "precio": forms.NumberInput(attrs={"placeholder": "Ingresa el precio de tu voluntariado"}),
            "imagen": forms.TextInput(attrs={"placeholder": "Ingresa una imagen de tu voluntariado"}),
        }
