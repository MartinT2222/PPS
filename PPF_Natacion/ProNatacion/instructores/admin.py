from django.contrib import admin

from instructores.models import Especialidade, Instructor, Agenda

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    
class InstructorAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'telefono',
    ]
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'instructor', 'horario'
    ]
    
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Agenda, AgendaAdmin)