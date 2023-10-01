# horarios/urls.py
from django.urls import path
from . import views

app_name = 'horarios'

urlpatterns = [
    # Agrega aquí las URLs para los horarios y clases
    path('clases/', views.lista_clases, name='lista_clases'),
    path('clases/<int:clase_id>/', views.detalle_clase, name='detalle_clase'),
    path('horarios/', views.lista_horarios, name='lista_horarios'),
    path('horarios/<int:horario_id>/', views.detalle_horario, name='detalle_horario'),
]
