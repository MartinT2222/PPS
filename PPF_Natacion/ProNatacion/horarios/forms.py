# forms.py

from django import forms
from .models import Clase
from instructores.models import Instructor

class ClaseForm(forms.ModelForm):
    # Agrega el campo de especialidad del instructor
    especialidad = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = Clase
        fields = ['especialidad', 'fecha', 'hora_inicio', 'hora_fin']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }
