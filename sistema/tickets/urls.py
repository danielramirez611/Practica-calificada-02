from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_solicitudes, name='lista_solicitudes'),  # Ruta vacía para la lista de servicios como vista principal
    path('servicios/', views.lista_servicios, name='lista_servicios'),  # Ruta para la lista de servicios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),  # Ruta para la lista de usuarios
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),  # Ruta para la lista de solicitudes
]
