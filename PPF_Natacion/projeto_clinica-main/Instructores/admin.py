from django.contrib import admin

from Instructores.models import TipoDeClase, Instructor, Agenda

class TipoDeClaseAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'TipoDeClase']

    
class AgendaAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'dia', 'horario']

    
admin.site.register(TipoDeClase, TipoDeClaseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Agenda, AgendaAdmin)