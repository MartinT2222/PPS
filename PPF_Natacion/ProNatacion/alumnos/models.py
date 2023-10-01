from django.db import models
from cuentas.models import Usuario
from horarios.models import Clase

class Alumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario.get_full_name()
    
class ProgresoAlumno(models.Model):
    progreso_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase_id = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_progreso = models.DateField()
    descripcion_progreso = models.TextField()

    def __str__(self):
        return f'Progreso para {self.alumno.usuario.get_full_name()} en {self.fecha_progreso}'