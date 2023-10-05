from django.db import models
from cuentas.models import User
from horarios.models import Clase
from django.core.validators import RegexValidator
from django.db.models.fields.related import ForeignKey, OneToOneField
from instructores.models import Agenda

class Alumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    SEXO = (
        ("MAS", "Maculino"),
        ("FEM", "Feminino")
    )
    sexo = models.CharField(max_length=9, choices=SEXO,)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número debe estar en este formato: \
                        '+99 99 9999-0000'.")

    telefono = models.CharField(verbose_name="Teléfono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    def __str__(self):
        return self.User.get_full_name()
    
class ProgresoAlumno(models.Model):
    progreso_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase_id = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_progreso = models.DateField()
    descripcion_progreso = models.TextField()

    def __str__(self):
        return f'Progreso para {self.alumno.User.get_full_name()} en {self.fecha_progreso}'
    
class Consulta(models.Model):
    agenda = OneToOneField(Agenda, on_delete=models.CASCADE, related_name='consulta')
    alumno = ForeignKey(Alumno, on_delete=models.CASCADE, related_name='consulta')
    
    class Meta:
        unique_together = ('agenda', 'alumno')
        
    def __str__(self):
        return f'{self.agenda} - {self.alumno}'
