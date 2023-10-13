from django.db import models

class ClaseNatacion(models.Model):
    clase_id = models.IntegerField(unique=True)
    especialidad = models.CharField(max_length=100)  # Nombre de la especialidad
    nombre_docente = models.CharField(max_length=100)  # Nombre del docente a cargo
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de la clase
    tipo_pago = models.CharField(max_length=20)  # Tipo de pago (efectivo, tarjeta, etc.)
    plan_elegido = models.CharField(max_length=100)  # Plan elegido para la clase
    fecha_clase = models.DateField()  # Fecha en que se dicta la clase
    horas_clase = models.TimeField()  # Horas en que se dicta la clase

    def __str__(self):
        return self.especialidad

class Alumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    fecha_inscripcion = models.DateField()
    telefono_emergencia = models.CharField(max_length=15)
    mensualidad = models.DecimalField(max_digits=10, decimal_places=2)
    membresia_vip = models.BooleanField(default=False)
    alergias = models.TextField(blank=True, null=True)
    docente_a_cargo = models.CharField(max_length=100, blank=True, null=True)
    clase_natacion = models.ForeignKey(ClaseNatacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    