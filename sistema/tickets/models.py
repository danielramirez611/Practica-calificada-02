from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField
import datetime

class Servicio(models.Model):
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    image = ImageField(upload_to="tickets/images")
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    image = ImageField(upload_to="tickets/images", default='default_image.jpg')
    email = models.EmailField()
    telefono = models.CharField(max_length=20, default='')  # Empty string as default value

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Aceptada', 'Aceptada'),
        ('Rechazada', 'Rechazada'),
    )

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    descripcion = models.TextField()
    date = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Solicitud de {self.persona} para {self.servicio}"
