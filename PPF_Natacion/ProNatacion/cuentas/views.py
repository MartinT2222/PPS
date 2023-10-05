from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.generic import CreateView, UpdateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import FormularioCreacionUsuarioAdmin

# Vista para la página de inicio
class VistaInicio(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'cuentas/index.html'
    login_url = reverse_lazy('cuentas:login')

    def get_object(self):
        return self.request.user

# Vista para iniciar sesión
class IniciarSesion(LoginView):
    model = User
    template_name = 'cuentas/update_password.html'

# Vista para cerrar sesión
class CerrarSesion(LogoutView):
    template_name = 'cuentas/logged_out.html'

# Vista para registrar un nuevo usuario
class VistaRegistro(CreateView):
    model = User
    template_name = 'cuentas/registro.html'
    form_class = FormularioCreacionUsuarioAdmin
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.info(self.request, "¡Registro exitoso! Inicie sesión.")
        return super().form_valid(form)

# Vista para solicitar restablecimiento de contraseña
def solicitud_reset_contrasena(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Solicitud de Restablecimiento de Contraseña"
                    email_template_name = "cuentas/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Django E-commerce',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, "admin@ejemplo.com", [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Encabezado no válido.')
                    return redirect('cuentas:password_reset_done')
    form = PasswordResetForm()
    return render(request=request, template_name="cuentas/password/password_reset.html", context={"form": form})

# Vista para actualizar los datos del usuario
class VistaActualizarUsuario(LoginRequiredMixin, UpdateView):
    model = User
    login_url = reverse_lazy('cuentas:login')
    template_name = 'cuentas/update_user.html'
    fields = ['nombre', 'email']
    success_url = reverse_lazy('cuentas:index')

    def get_object(self):
        return self.request.user

# Vista para actualizar la contraseña del usuario
class VistaActualizarContrasena(LoginRequiredMixin, FormView):
    template_name = 'cuentas/update_password.html'
    login_url = reverse_lazy('cuentas:login')
    success_url = reverse_lazy('cuentas:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(VistaActualizarContrasena, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(VistaActualizarContrasena, self).form_valid(form)

# Asignación de nombres a las vistas de clase para las URLs
index = VistaInicio.as_view()
login = IniciarSesion.as_view()
logout = CerrarSesion.as_view()
registro = VistaRegistro.as_view()
update_user = VistaActualizarUsuario.as_view()
update_password = VistaActualizarContrasena.as_view()



