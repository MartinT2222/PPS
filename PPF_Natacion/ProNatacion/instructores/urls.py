from django.urls import path
from .views import lista_instructores, detalle_instructor, InstructorDetailView

app_name = 'instructor'

urlpatterns = [
    path('', lista_instructores, name='lista_instructores'),
    path('<int:instructor_id>/', detalle_instructor, name='detalle_instructor'),
    path('perfil/', InstructorDetailView.as_view(), name='perfil'),
]
