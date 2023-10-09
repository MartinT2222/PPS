from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ClaseNatacion, Alumno
from .forms import AlumnoForm, ClaseNatacionForm
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.query_utils import Q



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


def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'tienda/lista_alumnos.html', {'alumnos': alumnos})




def detalle_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    return render(request, 'detalle_alumno.html', {'alumno': alumno})


@permission_required('TIENDA.agregar_alumno')
def agregar_alumno_y_clase(request):
    if request.method == 'POST':
        # Si el formulario de alumno es enviado
        if 'alumno_form' in request.POST:
            alumno_form = AlumnoForm(request.POST)
            if alumno_form.is_valid():
                # Guardar el alumno en la base de datos
                alumno = alumno_form.save()
                # Redireccionar o hacer lo que necesites con el alumno

        # Si el formulario de clase de natación es enviado
        elif 'clase_natacion_form' in request.POST:
            clase_natacion_form = ClaseNatacionForm(request.POST)
            if clase_natacion_form.is_valid():
                # Guardar la clase de natación en la base de datos
                clase_natacion = clase_natacion_form.save()
                # Redireccionar o hacer lo que necesites con la clase de natación
    else:
        alumno_form = AlumnoForm()
        clase_natacion_form = ClaseNatacionForm()

    return render(request, 'tienda/agregar_alumno_y_clase.html', {
        'alumno_form': alumno_form,
        'clase_natacion_form': clase_natacion_form,
    })



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

@permission_required('TIENDA.delete_alumno')
def eliminar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    alumno.delete()
    return redirect("tienda:home")