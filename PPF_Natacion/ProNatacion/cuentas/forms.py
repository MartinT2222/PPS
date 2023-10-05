from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class FormularioCreacionUsuarioAdmin(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'nombre', 'email']

class FormularioAdminUsuario(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']
