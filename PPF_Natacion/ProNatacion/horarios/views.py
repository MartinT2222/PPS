from django.shortcuts import render, get_object_or_404
from .models import Clase, HorarioClase


def lista_clases(request):
    # Obtener todas las clases
    clases = Clase.objects.all()
    return render(request, 'horarios/lista_clases.html', {'clases': clases})
def detalle_clase(request, clase_id):
    # Obtener una clase por su ID
    clase = get_object_or_404(Clase, pk=clase_id)
    # Obtener los horarios de esa clase
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
