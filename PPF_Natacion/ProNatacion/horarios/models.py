from django.db import models

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

    def __str__(self):
        return self.nombre