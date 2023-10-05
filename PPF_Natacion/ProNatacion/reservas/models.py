from django.db import models
from alumnos.models import Alumno
from horarios.models import Clase

class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()

    def __str__(self):
        return f'Reserva {self.reserva_id} - Alumno: {self.alumno.User.get_full_name()} - Clase: {self.clase.nombre}'
