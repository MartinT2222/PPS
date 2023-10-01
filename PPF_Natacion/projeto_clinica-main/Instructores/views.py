from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Instructor, Agenda, TipoDeClase


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")

class InstructorCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Instructor
    login_url = 'accounts:login'
    template_name = 'Instructores/cadastro.html'
    fields = ['nome', 'email', 'telefone', 'TipoDeClase']
    success_url = reverse_lazy('Instructores:Instructores_lista')
    
class InstructorListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'Instructores/Instructores_list.html'

    def get_queryset(self):
        return Instructor.objects.all().order_by('-pk')
    
class TipoDeClaseCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = TipoDeClase
    login_url = 'accounts:login'
    template_name = 'Instructores/cadastro.html'
    fields = ['nome',]
    success_url = reverse_lazy('Instructores:TipoDeClase_lista')
    
class TipoDeClaseListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'Instructores/TipoDeClase_list.html'

    def get_queryset(self):
        return TipoDeClase.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'Instructores/agenda_cadastro.html'
    fields = ['Instructores', 'dia', 'horario']
    success_url = reverse_lazy('Instructores:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'Instructores/agenda_cadastro.html'
    fields = ['Instructor', 'dia', 'horario']
    success_url = reverse_lazy('Instructores:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('Instructores:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('Instructores:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'Instructores/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')
    
Instructor_cadastro = InstructorCreateView.as_view()
Instructor_lista = InstructorListView.as_view()
TipoDeClase_cadastro = TipoDeClaseCreateView.as_view()
TipoDeClase_lista = TipoDeClaseListView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()

