from django.urls import path
from . import views  # Importa tus vistas desde tu aplicación

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista index
     path("registro/", views.registro, name="registro"),  # Ruta para la vista registro
    path('accounts/login/', views.loginUser, name='login'),  # Ruta para la vista login
    path("home/", views.home, name="home"), #Ruta para la vista home
    path("perfil/", views.edit_profile, name="perfil"), #Ruta para la vista perfil
    path('estudiante/', views.estudiante, name='estudiante'), #Ruta para la vista Estudiante
    path('bitacora/', views.Bitacora, name='bitacora'),
    path('anamnesis/', views.anamnesis, name='anamnesis'),
]