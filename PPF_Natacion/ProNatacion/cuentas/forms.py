from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class FormularioCreacionUsuarioAdmin(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'email']

class FormularioAdminUsuario(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'is_active', 'is_staff']
