from django.urls import path
from . import views

app_name = 'Instructores'

urlpatterns = [
    path('registro/Instructor/', views.Instructor_cadastro, name='Instructor_cadastro'),
    path('registro/TipoDeClase/', views.TipoDeClase_cadastro, name='TipoDeClase_cadastro'),
    path('agendar/', views.agenda_cadastro, name='agendar_consulta'),
    path('agendar/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_consulta_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),
    path('minhas/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/Instructores/', views.Instructor_lista, name="Instructores_lista"),
    path('admim/lista/TipoDeClase/', views.TipoDeClase_lista, name="TipoDeClase_lista")
    
]