from django.db import models

# Create your models here.
class Proveedor(models.Model):
     nombre = models.CharField(max_length=200)

     def __str__(self):
         return self.nombre

class TipoVehiculo(models.Model):
    nombre =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
class MarcaVehiculo(models.Model):
    nombre =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
class EstadoVehiculo(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado


class Vehiculos(models.Model):
    modelo = models.CharField(max_length=200)
    linea = models.CharField(max_length=100)
    centimetros_cubicos = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to = "imagenes/", blank=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True, related_name='tipo_vehiculo')
    marca = models.ForeignKey(MarcaVehiculo, on_delete=models.CASCADE, null=True, blank=True, related_name='marca')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True, related_name='proveedor')
    estado = models.ForeignKey(EstadoVehiculo, on_delete=models.CASCADE, null=True, blank=True, related_name='estado_vehiculo')

    def __str__(self):
        return self.modelo

