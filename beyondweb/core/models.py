from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

class bodega_ubicacion(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    
    stock = models.PositiveIntegerField(default=0)
    bodega_ubicacion = models.ForeignKey(bodega_ubicacion, on_delete=models.SET_NULL, null=True, blank=True)

    # Imágenes
    imagen1 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen2 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen3 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen4 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen5 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen6 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen7 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen8 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen9 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen10 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen11 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen12 = models.ImageField(upload_to="productos/", blank=True, null=True)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_producto