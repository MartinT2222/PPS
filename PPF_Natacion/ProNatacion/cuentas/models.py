import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, Permission






class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico debe estar configurado')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Los superusuarios deben tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Los superusuarios deben tener is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class Usuario(AbstractBaseUser):
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

    groups = models.ManyToManyField(
        Group,
        verbose_name='Grupos',
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        related_name='user_set',
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Permisos de usuario',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        related_name='user_set',
        related_query_name='user'
    )