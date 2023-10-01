from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Alumno, ProgresoAlumno

def lista_alumnos(request):
    # Obtener todos los alumnos
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})

def detalle_alumno(request, alumno_id):
    # Obtener un alumno por su ID
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    return render(request, 'alumnos/detalle_alumno.html', {'alumno': alumno})

def lista_progresos_alumno(request, alumno_id):
    # Obtener todos los progresos de un alumno
    progresos = ProgresoAlumno.objects.filter(alumno_id=alumno_id)
    return render(request, 'alumnos/lista_progresos_alumno.html', {'progresos': progresos})

def detalle_progreso(request, progreso_id):
    # Obtener un progreso por su ID
    progreso = get_object_or_404(ProgresoAlumno, pk=progreso_id)
    return render(request, 'alumnos/detalle_progreso.html', {'progreso': progreso})
