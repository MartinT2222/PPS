from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey

class TipoDeClase(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'
    
class Instructor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    email = models.EmailField(verbose_name="Email")
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número debe estar en este formato: \
                '+99 99 9999-0000'.")

    telefono = models.CharField(verbose_name="Telefono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    
    TipoDeClase = ForeignKey(TipoDeClase,
                              on_delete=models.CASCADE,
                              related_name='instructores')
    
    def __str__(self):
        return f'{self.nombre}'


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No se puede elegir una fecha pasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Elija un día laborable.')

class Agenda(models.Model):
    instructor = ForeignKey(Instructor, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Ingrese una fecha para la agenda", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "09:00 a.m. - 10:00 a.m."),
        ("2", "10:00 a.m. - 11:00 a.m."),
        ("3", "11:00 a.m. - 12:00 p.m."),
        # Agrega más horarios según sea necesario
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        unique_together = ('horario', 'dia')
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.instructor}'
