from django.db import models
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta ,time  
from django.utils import timezone

class HorarioClase(models.Model):
    horario_id = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f'Horario {self.horario_id} - {self.dia_semana} de {self.hora_inicio} a {self.hora_fin}'


class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField(default=time(23, 59, 59))  # Valor predeterminado: 23:59:59

    def save(self, *args, **kwargs):
        if self.fecha and self.hora_inicio:
            # Combina la fecha y la hora de inicio para obtener la hora completa
            fecha_hora_inicio = datetime.combine(self.fecha, self.hora_inicio)

            # La duración es de 30 días (un mes)
            fecha_hora_fin = fecha_hora_inicio + timedelta(days=30)

            # Asigna la hora de inicio y fin calculadas
            self.hora_inicio = fecha_hora_inicio.time()
            self.hora_fin = fecha_hora_fin.time()

        super().save(*args, **kwargs)


def detalle_clase(request, clase_id):
    # Obtener una clase por su ID
    clase = get_object_or_404(Clase, pk=clase_id)
    # Obtener los horarios de esa clase
    horarios = HorarioClase.objects.filter(clase=clase)  # Asumiendo que HorarioClase tiene un campo 'clase' para relacionarlos

    return render(request, 'horarios/detalle_clase.html', {'clase': clase, 'horarios': horarios})
