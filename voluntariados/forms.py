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
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre del voluntariado"}),
            "area": forms.TextInput(attrs={"placeholder": "Área del voluntariado"}),
            "duracion": forms.TextInput(attrs={"placeholder": "Duración del voluntariado"}),
            "descripcion": forms.Textarea(attrs={"placeholder": "Descripción del voluntariado",
                                                 "rows":4, "cols":50}),
            "lugar": forms.TextInput(attrs={"placeholder": "Lugar del voluntariado"}),
            "precio": forms.NumberInput(attrs={"placeholder": "Precio del voluntariado"}),
            "imagen": forms.TextInput(attrs={"placeholder": "Imagen del voluntariado"}),
        }
