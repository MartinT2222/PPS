from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from .forms import FormularioCreacionUsuarioAdmin, FormularioAdminUsuario
from django.contrib.auth.models import Group, Permission

class AdminUsuario(BaseUserAdmin):
    add_form = FormularioAdminUsuario
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = FormularioCreacionUsuarioAdmin
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Información Básica: ', {
            'fields': ('nombre', 'date_joined')
        }),
        ('Permisos: ', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
    )
    list_display = ['username', 'email', 'is_active', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'is_active', 'tipo_usuario']
    filter_horizontal = ('groups', 'user_permissions',)  # Corrección aquí


# Registrar el modelo Usuario con su administrador personalizado

admin.site.register(Usuario, AdminUsuario)
