from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('alumno/<int:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    path('alumno/<int:alumno_id>/progresos/', views.lista_progresos_alumno, name='lista_progresos_alumno'),
    path('progreso/<int:progreso_id>/', views.detalle_progreso, name='detalle_progreso'),
]
