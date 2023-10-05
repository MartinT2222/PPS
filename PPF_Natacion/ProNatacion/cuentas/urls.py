from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from . import views

# Nombre de la aplicación
app_name = 'cuentas'

# Definición de las URL
urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('editar-datos/', views.update_user, name='update_user'),  # Actualizar datos de usuario
    path('cambiar-contrasena/', views.actualizar_contrasena, name='cambiar_contrasena'),  # Cambiar contraseña
    path('registro/', views.registro, name='registro'),  # Página de registro
    path('entrar/', views.login, name='login'),  # Página de inicio de sesión
    path('cerrar-sesion/', views.logout, name='logout'),  # Página para cerrar sesión
    path('recuperar-contrasena/',views.solicitud_reset_contrasena,name='solicitud_reset_contrasena'),# Página para solicitar restablecimiento de contraseña
    path('recuperar-contrasena-ok/',auth_views.PasswordResetDoneView.as_view(template_name='cuentas/contrasena/reset_contrasena_ok.html'),name='reset_contrasena_ok',),# Página de confirmación de solicitud de restablecimiento de contraseña
    path('recuperar-contrasena-completo/',auth_views.PasswordResetDoneView.as_view(template_name='cuentas/contrasena/reset_contrasena_completo.html'),name='reset_contrasena_completo', ),# Página de confirmación completa de restablecimiento de contraseña
    path('recuperar-contrasena-confirmar/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='cuentas/contrasena/reset_contrasena_confirmar.html',
            success_url=reverse_lazy("cuentas:reset_contrasena_completo")
        ),
        name='reset_contrasena_confirmar'  # Página para confirmar restablecimiento de contraseña
    ),
    path(
        'recuperar-contrasena_confirmar',
        views.solicitud_reset_contrasena,
        name="solicitud_reset_contrasena"  # Página para solicitar restablecimiento de contraseña
    )
]

# Configuración para servir archivos estáticos durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
