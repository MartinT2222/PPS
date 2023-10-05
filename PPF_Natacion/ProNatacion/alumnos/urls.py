from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    path('registro/', views.cliente_crear, name='cliente_cadastro'),
    path('atualizar/', views.cliente_actualizar, name='cliente_atualizar'),
    path('consultas/', views.consulta_lista, name='consulta_list'),
    path('consultas/criar/', views.consulta_create, name='consulta_create'),
    path('consultas/editar/<int:pk>/', views.consulta_actualizar, name='consulta_update'),
    path('consultas/excluir/<int:pk>/', views.consulta_eliminar, name='consulta_delete'),
]