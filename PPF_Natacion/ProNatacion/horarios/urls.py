# horarios/urls.py
from django.urls import path
from . import views
from horarios.views import detalle_clase

app_name = 'horarios'

urlpatterns = [
    # Agrega aquí las URLs para los horarios y clases
    path('horarios/', views.listar_horarios_clase, name='listar_horarios_clase'),
    path('clase/<int:clase_id>/', detalle_clase, name='detalle_clase'),
]
