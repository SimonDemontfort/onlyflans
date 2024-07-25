from django.db import models
import uuid
# Create your models here.

class FormPresupuesto (models.Model):
    nombre = models.CharField(max_length= 64)
    correo = models.CharField(max_length=30)
    productos = models.CharField(max_length=260)



class Flan(models.Model):
    flan_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        max_length=64
    )
    description = models.TextField()
    precio = models.IntegerField(default=5000)
    image_url = models.URLField()
    is_private = models.BooleanField()
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mensaje = models.TextField()
    
    def __str__(self):
        name = self.nombre
        message = self.mensaje
        return f'{name} : {message}'