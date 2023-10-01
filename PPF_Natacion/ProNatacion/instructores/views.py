from django.shortcuts import render, get_object_or_404
from .models import Instructor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

def lista_instructores(request):
    instructores = Instructor.objects.all()
    return render(request, 'instructores/lista_instructores.html', {'instructores': instructores})

def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    return render(request, 'instructores/detalle_instructor.html', {'instructor': instructor})

@method_decorator(login_required, name='dispatch')
class InstructorDetailView(View):
    def get(self, request, *args, **kwargs):
        # Obtenemos el perfil del instructor asociado al usuario actual
        instructor_profile = get_object_or_404(Instructor, usuario=request.user)
        return render(request, 'instructor/detail.html', {'instructor_profile': instructor_profile})
