from django.shortcuts import render, get_object_or_404
from .models import Servicio, Persona, Solicitud


def lista_solicitudes(request):
    servicios = Servicio.objects.all()
    solicitudes = Solicitud.objects.all()

    servicio_filtrado = request.GET.get('servicio')
    if servicio_filtrado:
        solicitudes = solicitudes.filter(servicio__nombre=servicio_filtrado)

    context = {
        'solicitudes': solicitudes,
        'servicios': servicios
    }
    return render(request, 'lista_solicitudes.html', context)

def lista_servicios(request):
    # Obtiene todos los servicios
    servicios = Servicio.objects.all()
    return render(request, 'lista.html', {'servicios': servicios})

def lista_usuarios(request):
    # Obtiene todos los usuarios
    usuarios = Persona.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def lista_solicitudes(request):
    # Obtiene todas las solicitudes
    solicitudes = Solicitud.objects.all()
    return render(request, 'lista_solicitudes.html', {'solicitudes': solicitudes})
