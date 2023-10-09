from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('clases/', views.lista_clases_natacion, name='lista_clases_natacion'),
    path('clases/<int:clase_id>/', views.detalle_clase_natacion, name='detalle_clase_natacion'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('buscar/', views.buscar, name = 'buscar'),
    path('alumnos/<int:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    
    path('alumnos/agregar/', views.agregar_alumno_y_clase, name='agregar_alumno_y_clase'),
    path('alumnos/editar/<int:alumno_id>/', views.editar_alumno, name='edit_alumno'),
    path('alumnos/eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
]
