from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('conta/', include('cuentas.urls', namespace='cuentas')),
    path('alumnos/', include('alumnos.urls', namespace="alumnos")),
    path('instructores/', include('instructores.urls', namespace="instructores")),
    path('horarios/', include('horarios.urls', namespace='horarios')),
    path('reservas/', include('reservas.urls', namespace='reservas')),
]
