from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class ModelBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # Si `username` es None, intentamos obtenerlo de kwargs utilizando el campo especificado en USERNAME_FIELD del modelo de usuario personalizado
        if username is None:
            username = kwargs.get(Usuario.USERNAME_FIELD)
        
        try:
            # Intentamos obtener al usuario usando el campo `email` en lugar de `username`
            usuario = Usuario.objects.get(email=username)
            # Verificamos la contraseña
            if usuario.check_password(password):
                return usuario
        except Usuario.DoesNotExist:
            # Si el usuario no existe, retornamos None
            return None
