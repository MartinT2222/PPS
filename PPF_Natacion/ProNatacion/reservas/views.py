from django.shortcuts import render, get_object_or_404
from .models import Reserva

def lista_reservas(request):
    # Obtener todas las reservas
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def detalle_reserva(request, reserva_id):
    # Obtener una reserva por su ID
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'reservas/detalle_reserva.html', {'reserva': reserva})
