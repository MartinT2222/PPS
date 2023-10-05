from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Instructor, Agenda, Especialidade



class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("cuentas:index")

class InstructorCrearView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Instructor
    login_url = 'cuentas:login'
    template_name = 'instructores/cadastro.html'
    fields = ['nombre', 'email', 'telefono', 'especialidade']
    success_url = reverse_lazy('instructores:instructores_lista')

class InstructorListaView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'cuentas:login'
    template_name = 'instructores/instructores_list.html'

    def get_queryset(self):
        return Instructor.objects.all().order_by('-pk')
    

class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Especialidade
    login_url = 'cuentas:login'
    template_name = 'instructores/cadastro.html'
    fields = ['nombre',]
    success_url = reverse_lazy('instructores:especialidade_lista')

class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'cuentas:login'
    template_name = 'instructores/especialidade_list.html'

    def get_queryset(self):
        return Especialidade.objects.all().order_by('-pk')


class AgendaCrearView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'cuentas:login'
    template_name = 'instructores/agenda_cadastro.html'
    fields = ['instructor', 'dia', 'horario']
    success_url = reverse_lazy('instructores:agenda_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AgendaActualizarView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'cuentas:login'
    template_name = 'instructores/agenda_cadastro.html'
    fields = ['instructor', 'dia', 'horario']
    success_url = reverse_lazy('instructores:agenda_lista')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AgendaEliminarView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('instructores:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('instructores:agenda_lista')


class AgendaListaView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    login_url = 'cuentas:login'
    template_name = 'instructores/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')



instructor_cadastro = InstructorCrearView.as_view()
instructor_lista = InstructorListaView.as_view()
especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()
agenda_cadastro = AgendaCrearView.as_view()
agenda_actualizar = AgendaActualizarView.as_view()
agenda_lista = AgendaListaView.as_view()
agenda_eliminar = AgendaEliminarView.as_view()
