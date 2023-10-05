from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alumno, Consulta


class ClienteCrearView(LoginRequiredMixin, CreateView):
    
    model = Alumno
    template_name = 'alumnos/cadastro.html'
    fields = ['sexo', 'telefono','fecha_nacimiento', 'direccion']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClienteActualizarView(LoginRequiredMixin, UpdateView):

    model = Alumno
    login_url = reverse_lazy('cuentas:login')
    template_name = 'cuentas/update_user.html'
    fields = ['sexo', 'telefono', 'fecha_nacimiento', 'direccion']
    success_url = reverse_lazy('cuentas:index')

    def get_object(self):
        user = self.request.user
        try:
            return Alumno.objects.get(user=user)
        except Alumno.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class ConsultaCrearView(LoginRequiredMixin, CreateView):

    model = Consulta
    login_url = 'cuentas:login'
    template_name = 'alumnos/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('alumnos:consulta_list')
    
    def form_valid(self, form):
        try:
            form.instance.alumno = Alumno.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'No puedes marcar esta consulta')
                return HttpResponseRedirect(reverse_lazy('alumnos:consulta_create'))
        except Alumno.DoesNotExist:
            messages.warning(self.request, 'Completa tu perfil')
            return HttpResponseRedirect(reverse_lazy('alumnos:cliente_cadastro'))
        messages.info(self.request, 'Consulta marcada con éxito')
        return HttpResponseRedirect(reverse_lazy('alumnos:consulta_list'))
    
class ConsultaActualizarView(LoginRequiredMixin, UpdateView):

    model = Consulta
    login_url = 'cuentas:login'
    template_name = 'alumnos/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('instructores:consulta_lista')
    
    def form_valid(self, form):
        form.instance.alumno = Alumno.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class ConsultaEliminarView(LoginRequiredMixin, DeleteView):
    model = Consulta
    success_url = reverse_lazy('alumnos:consulta_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta eliminada exitosamente")
        return reverse_lazy('alumnos:consulta_list')


class ConsultaListaView(LoginRequiredMixin, ListView):
    
    login_url = 'cuentas:login'
    template_name = 'alumnos/consulta_list.html'

    def get_queryset(self):
        User = self.request.user
        try:
            alumno = Alumno.objects.get(User=User)
        except Alumno.DoesNotExist:
            messages.warning(self.request, 'Crea una consulta')
            return None
        try:
            consultas = Consulta.objects.filter(alumno=alumno).order_by('-pk')
        except Consulta.DoesNotExist:
            messages.warning(self.request, 'Crea una consulta')
            return None
        return consultas


cliente_crear = ClienteCrearView.as_view()
cliente_actualizar = ClienteActualizarView.as_view()
consulta_lista = ConsultaListaView.as_view()
consulta_create = ConsultaCrearView.as_view()
consulta_actualizar = ConsultaActualizarView.as_view()
consulta_eliminar = ConsultaEliminarView.as_view()
