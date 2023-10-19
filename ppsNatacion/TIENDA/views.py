from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ClaseNatacion, Alumno
from .forms import AlumnoForm, ClaseNatacionForm
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def home(request):
    # Aquí puedes agregar la lógica que desees para la página de inicio
    # Por ejemplo, podrías obtener algunos datos de la base de datos y pasarlos a la plantilla
    # Luego renderiza la plantilla y envía los datos como contexto

    # Ejemplo de datos (puedes personalizar estos datos según tu aplicación)
    data = {
        'titulo': 'Bienvenido a nuestro sitio',
        'mensaje': 'Esto es un mensaje de bienvenida',
        # Otros datos que desees enviar a la plantilla
    }

    # Renderiza la plantilla y envía el contexto
    return render(request, 'tienda/index.html', data)



def buscar(request):
    buscar = request.GET['buscar']
    alumno = Alumno.objects.filter(
        Q(descripcion__icontains=buscar) | Q(titulo__icontains=buscar))

    return render(request, 'tienda/buscar.html', {

        'alumno': alumno,

    })



def lista_clases_natacion(request):
    clases = ClaseNatacion.objects.all()
    return render(request, 'lista_clases_natacion.html', {'clases': clases})

def detalle_clase_natacion(request, clase_id):
    clase = get_object_or_404(ClaseNatacion, pk=clase_id)
    return render(request, 'detalle_clase_natacion.html', {'clase': clase})


@permission_required('TIENDA.lista_alumnos')
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'tienda/lista_alumnos.html', {'alumnos': alumnos})




def detalle_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    return render(request, 'detalle_alumno.html', {'alumno': alumno})


#@permission_required('TIENDA.agregar_alumno_y_clase')
#def agregar_alumno_y_clase(request):
#    alumno_form = None
#    clase_natacion_form = None
#    if request.method == 'POST':
#        # Si el formulario de alumno es enviado
#        if 'alumno_form' in request.POST:
#            alumno_form = AlumnoForm(request.POST)
#            if alumno_form.is_valid():
#                # Guardar el alumno en la base de datos
#                alumno = alumno_form.save()
                # Redireccionar o hacer lo que necesites con el alumno

#        # Si el formulario de clase de natación es enviado
#        elif 'clase_natacion_form' in request.POST:
#            clase_natacion_form = ClaseNatacionForm(request.POST)
#            if clase_natacion_form.is_valid():
#                # Guardar la clase de natación en la base de datos
#                # Redireccionar o hacer lo que necesites con la clase de natación
#                clase_natacion = clase_natacion_form.save(commit=False)
#                clase_natacion.clase_id = clase_natacion_form.cleaned_data.get('clase_id')  # Aquí debes asignar el valor correcto
#                clase_natacion.save()  # Ahora puedes guardarla en la base de datos
#    else:
#        alumno_form = AlumnoForm()
#        clase_natacion_form = ClaseNatacionForm()

#    return render(request, 'tienda/agregar_alumno_y_clase.html', {
#        'alumno_form': alumno_form,
#        'clase_natacion_form': clase_natacion_form,
#    })


@permission_required('TIENDA.agregar_alumno')
def agregar_alumno(request):
    if request.method == 'POST':
        if 'alumno_form' in request.POST:
            alumno_form = AlumnoForm(request.POST)
            if alumno_form.is_valid():
                # Guardar el alumno en la base de datos
                alumno = alumno_form.save()
                # Obtener los datos del alumno
                datos_alumno = {
                    'alumno_id': alumno.alumno_id,
                    'nombre': alumno.nombre,
                    'direccion': alumno.direccion,
                    'telefono': alumno.telefono,
                    'sexo': alumno.get_sexo_display(),
                    'edad': alumno.edad,
                    'email': alumno.email,
                    'fecha_inscripcion': alumno.fecha_inscripcion.strftime('%Y-%m-%d'),  # Formatear a 'YYYY-MM-DD'
                    'telefono_emergencia': alumno.telefono_emergencia,
                    'mensualidad': str(alumno.mensualidad),  # Convertir a cadena para mostrar
                    'membresia_vip': 'Sí' if alumno.membresia_vip else 'No',  # Convertir a 'Sí' o 'No'
                    'alergias': alumno.alergias,
                    'docente_a_cargo': alumno.docente_a_cargo,
                    'clase_natacion': alumno.clase_natacion.especialidad if alumno.clase_natacion else ''

                    # Agrega más datos según los que quieras mostrar
                }
                return render(request, 'tienda/agregar_alumno.html', {'alumno_form': alumno_form, 'datos_alumno': datos_alumno})
    else:
        alumno_form = AlumnoForm()

    return render(request, 'tienda/agregar_alumno.html', {'alumno_form': alumno_form})


@permission_required('TIENDA.agregar_clase')
def agregar_clase(request):
    if request.method == 'POST':
        if 'clase_natacion_form' in request.POST:
                clase_natacion_form = ClaseNatacionForm(request.POST)
                if clase_natacion_form.is_valid():
                    # Guardar la clase de natación en la base de datos
                    # Redireccionar o hacer lo que necesites con la clase de natación
                    clase_natacion = clase_natacion_form.save(commit=False)
                    clase_natacion.clase_id = clase_natacion_form.cleaned_data.get('clase_id')  # Aquí debes asignar el valor correcto
                    clase_natacion.save()  # Ahora puedes guardarla en la base de datos
    else:
        clase_natacion_form = ClaseNatacionForm()

    return render(request, 'tienda/agregar_clase.html', {'clase_natacion_form': clase_natacion_form})


def crear_actualizar_alumno(request, alumno_id=None):
    # ... lógica para crear o actualizar un alumno ...

    # Obtener el alumno según el ID proporcionado
    alumno = get_object_or_404(Alumno, id=alumno_id)

    # Después de crear o actualizar el alumno, enviar el recordatorio de cuota
    alumno.enviar_recordatorio_cuota_whatsapp()

    # Verificar si el pago está marcado como pagado
    if alumno.pago:
        # Actualizar la fecha de inscripción si el pago está marcado como pagado
        alumno.fecha_inscripcion = timezone.now().date()
        alumno.save()
    
    # Resto del código para renderizar la página
    return render(request, 'tienda/lista_alumnos.html', {'alumnos': [alumno]})











@permission_required('TIENDA.edit_alumno')
def editar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_alumnos'))
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form, 'alumno': alumno})






@csrf_exempt
@permission_required('TIENDA.delete_alumno')
def eliminar_alumno(request, alumno_id):
    if request.method == 'POST':
        try:
            alumno = Alumno.objects.get(pk=alumno_id)
            print('Alumno encontrado:', alumno.nombre)
            alumno.delete()
            print('Alumno eliminado correctamente.')
            return JsonResponse({'message': 'Alumno eliminado correctamente.'}, status=200)
        except Alumno.DoesNotExist:
            print('No se encontró el alumno con ID:', alumno_id)
            return JsonResponse({'error': 'Alumno no encontrado.'}, status=404)
        except Exception as e:
            print('Ocurrió un error al eliminar el alumno:', str(e))
            return JsonResponse({'error': 'Error al eliminar el alumno.'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
