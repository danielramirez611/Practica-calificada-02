from django.contrib import admin
from .models import Persona,Servicio, Solicitud

# Register your models here.
admin.site.register(Persona)
admin.site.register(Servicio)
admin.site.register(Solicitud)
