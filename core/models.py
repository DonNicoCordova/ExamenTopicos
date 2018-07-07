from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100,default="Usuario Anonimo")
    apellido = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    telefono = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=100,blank=True)
    imagen = models.ImageField(upload_to="profileImages/",blank=True)