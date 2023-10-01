from django.db import models
from cuentas.models import Usuario


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='instructor_profile')
    especialidad = models.CharField('Especialidad', max_length=100)

    def __str__(self):
        return f'Instructor {self.usuario.username}'
