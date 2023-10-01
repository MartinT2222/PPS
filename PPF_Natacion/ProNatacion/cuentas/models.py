import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)

class Usuario(AbstractBaseUser,PermissionsMixin):
    TIPO_USUARIO_CHOICES = [
        ('administrativo', 'Administrativo'),
        ('instructor', 'Instructor'),
        ('alumno', 'Alumno'),
    ]

    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Correo electrónico', unique=True)
    username = models.CharField(
        'Nombre de usuario', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Proporcione un nombre de usuario válido. '
                'Este valor debe contener solo letras, números '
                'y los caracteres: @/./+/-/_.'
                ,  'inválido'
            )
        ], help_text='Un nombre corto que se usará'+
                    ' para identificarte de forma única en la plataforma.'
    )
    tipo_usuario = models.CharField('Tipo de Usuario', max_length=20, choices=TIPO_USUARIO_CHOICES)
    is_active = models.BooleanField('Activo', default=True)
    is_staff = models.BooleanField('Equipo', default=False)
    date_joined = models.DateTimeField('Fecha de registro', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre or self.username  

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]

    