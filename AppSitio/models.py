from django.db import models
from django.contrib.auth.models import User

import random


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Trabajo(models.Model):
    ot_nro = models.IntegerField(unique=True, blank=True, null=True)
    dispositivo = models.CharField(max_length=50)
    falla = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)
    estado_opciones = [
        ('Ingresado', 'Ingresado'),
        ('En reparación', 'En reparación'),
        ('Reparado', 'Reparado'),
        ('Sin solución', 'Sin solución'),
        ('Entregado', 'Entregado'),
    ]
    estado = models.CharField(max_length=50, choices=estado_opciones, default='Ingresado')
    

    def __str__(self):
        return f"OT: {self.ot_nro} -- {self.dispositivo} -- Estado: {self.estado}"

    def save(self, *args, **kwargs):                                                
        if not self.ot_nro:
            while True:
                random_ot = random.randint(100000, 999999)
                if not Trabajo.objects.filter(ot_nro=random_ot).exists():
                    self.ot_nro = random_ot
                    break
        super(Trabajo, self).save(*args, **kwargs)


class Publicacion(models.Model):
    producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    condicion_opciones = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
    ]
    condicion = models.CharField(max_length=50, choices=condicion_opciones)
    precio = models.IntegerField()
    vendedor = models.CharField(max_length=50)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        
    def __str__(self):
        return f"{self.producto} - {self.condicion} - ${self.precio}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   