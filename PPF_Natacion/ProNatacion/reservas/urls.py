from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('lista_reservas/', views.lista_reservas, name='lista_reservas'),
    path('detalle_reserva/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    # Agrega más URL según sea necesario para tu aplicación
]
