from django.contrib import admin
from .models import ProgresoAlumno
from .models import Alumno, Consulta


@admin.register(ProgresoAlumno)
class ProgresoAlumnoAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'get_clase', 'fecha_progreso']
    list_filter = ['alumno', 'clase_id__nombre', 'fecha_progreso']

    def get_clase(self, obj):
        return obj.clase_id.nombre

    get_clase.admin_order_field = 'clase_id__nombre'
    get_clase.short_description = 'Clase'


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'telefono', 'sexo', 'fecha_nacimiento', 'direccion',
    ]
    
class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'agenda', 'alumno',
    ]
    
    
admin.site.register(Alumno, ClientAdmin)
admin.site.register(Consulta, ConsultaAdmin)