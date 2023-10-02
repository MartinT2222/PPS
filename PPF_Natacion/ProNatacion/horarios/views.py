from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Clase, HorarioClase

# Vista para mostrar todos los horarios de clase
def listar_horarios_clase(request):
    horarios = HorarioClase.objects.all()
    horarios_list = [{'id': horario.horario_id,
                      'dia_semana': horario.dia_semana,
                      'hora_inicio': horario.hora_inicio.strftime('%H:%M'),
                      'hora_fin': horario.hora_fin.strftime('%H:%M')} for horario in horarios]
    return JsonResponse({'horarios': horarios_list})

# Vista para mostrar detalles de una clase y sus horarios
def detalle_clase(request, clase_id):
    clase = get_object_or_404(Clase, pk=clase_id)
    horarios = HorarioClase.objects.filter(clase=clase)
    return render(request, 'horarios/detalle_clase.html', {'clase': clase, 'horarios': horarios})





def lista_horarios(request):
    # Obtener todos los horarios de clase
    horarios = HorarioClase.objects.all()
    return render(request, 'horarios/lista_horarios.html', {'horarios': horarios})

def detalle_horario(request, horario_id):
    # Obtener un horario por su ID
    horario = get_object_or_404(HorarioClase, pk=horario_id)
    return render(request, 'horarios/detalle_horario.html', {'horario': horario})

# views.py

from django.shortcuts import render
from django.views import View
from instructores.models import Instructor
from .forms import ClaseForm

class CalendarioView(View):
    def get(self, request, instructor_id):
        # Obtiene la especialidad del instructor
        instructor = Instructor.objects.get(pk=instructor_id)
        especialidad = instructor.especialidad

        # Crea el formulario con la especialidad
        form = ClaseForm(initial={'especialidad': especialidad})

        return render(request, 'clases/calendario.html', {'form': form})
