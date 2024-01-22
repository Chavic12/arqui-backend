from django.db import models

# Create your models here.


class Inventario(models.Model):
    nombre = models.CharField(max_length=30)
    Ciudad = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - Ciudad: {self.Ciudad}"


class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    ubicacion = models.CharField(max_length=50)
    inventario = models.OneToOneField(
        Inventario, on_delete=models.CASCADE, related_name="almacen_inventario"
    )

    def __str__(self):
        return f"{self.nombre} - Ubicación: {self.ubicacion}"


class RolPersona(models.Model):
    rol = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.rol}"


class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    edad = models.IntegerField()
    rol = models.ForeignKey(
        RolPersona, on_delete=models.CASCADE, related_name="personal_rol"
    )
    inventario = models.ForeignKey(
        Inventario, on_delete=models.CASCADE, related_name="personal_inventario"
    )

    def __str__(self):
        return f"{self.nombre} - Edad: {self.edad} - Rol: {self.rol}"


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    inventario = models.ForeignKey(
        Inventario, on_delete=models.CASCADE, related_name="producto_inventario"
    )
    categoria = models.ForeignKey(
        CategoriaProducto, on_delete=models.CASCADE, related_name="producto_categoria"
    )
    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=30)
    novedad = models.CharField(max_length=50, null=True, blank=True)
    fechaEntrada = models.DateField()
    fechaCaducidad = models.DateField(null=True, blank=True)
    via_administrativa = models.CharField(max_length=30, null=True, blank=True)
    material = models.CharField(max_length=30, null=True, blank=True)
    instrucciones_almacenamiento = models.CharField(
        max_length=100, null=True, blank=True
    )
    instrucciones_uso = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad} - Estado: {self.estado}"
