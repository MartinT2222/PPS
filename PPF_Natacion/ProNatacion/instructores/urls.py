from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('registro/instructor/', views.instructor_cadastro, name='instructor_cadastro'),
    path('registro/tipo-de-clase/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('agendar/', views.agenda_cadastro, name='agendar_consulta'),
    path('agendar/actualizar/<int:pk>/', views.agenda_actualizar, name='agendar_consulta_atualizar'),
    path('agendar/eliminar/<int:pk>/', views.agenda_eliminar, name='agendar_consulta_deletar'),
    path('mis/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admin/lista/instructores/', views.instructor_lista, name="instructores_lista"),
    path('admin/lista/tipo-de-clase/', views.especialidade_lista, name="especialidade_lista")
]
