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

    def save_model(self, request, obj, form, change):
        # Llama al método de asignación de grupos y permisos al guardar el usuario
        self.assign_groups_and_permissions(obj)
        super().save_model(request, obj, form, change)

    def assign_groups_and_permissions(self, user):
        # Asignar grupos según el tipo de usuario
        if user.tipo_usuario == 'administrativo':
            admin_group, created = Group.objects.get_or_create(name='Administrativo')
            user.groups.set([admin_group])
        elif user.tipo_usuario == 'instructor':
            instructor_group, created = Group.objects.get_or_create(name='Instructor')
            user.groups.set([instructor_group])
        elif user.tipo_usuario == 'alumno':
            alumno_group, created = Group.objects.get_or_create(name='Alumno')
            user.groups.set([alumno_group])

        # Asignar permisos a los grupos
        if user.is_superuser:
            all_permissions = Permission.objects.all()
            for perm in all_permissions:
                admin_group.permissions.add(perm)
                instructor_group.permissions.add(perm)
        elif user.is_staff:
            # Asigna permisos específicos para el personal de la plataforma
            # Ajusta según tus necesidades
            # Por ejemplo:
            admin_group.permissions.add('is_superuser')
            # instructor_group.permissions.add('permiso2')

# Registrar el modelo Usuario con su administrador personalizado

admin.site.register(Usuario, AdminUsuario)
