from django.contrib import admin
from .models import (
    Inventario,
    Almacen,
    RolPersona,
    Personal,
    CategoriaProducto,
    Producto,
)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "Ciudad")
    search_fields = (
        "nombre",
        "Ciudad",
    )  # Agrega los campos que deseas habilitar para la búsqueda


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "email", "ubicacion", "inventario")
    search_fields = (
        "nombre",
        "ubicacion",
    )  # Agrega los campos que deseas habilitar para la búsqueda


@admin.register(RolPersona)
class RolPersonaAdmin(admin.ModelAdmin):
    list_display = ("rol",)
    search_fields = ("rol",)  # Agrega los campos que deseas habilitar para la búsqueda


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "email", "edad", "rol", "inventario")
    search_fields = (
        "nombre",
        "email",
    )  # Agrega los campos que deseas habilitar para la búsqueda


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = (
        "nombre",
    )  # Agrega los campos que deseas habilitar para la búsqueda


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "cantidad",
        "estado",
        "novedad",
        "fechaEntrada",
        "fechaCaducidad",
        "via_administrativa",
        "material",
        "instrucciones_almacenamiento",
        "instrucciones_uso",
        "inventario",
        "categoria",
    )
    search_fields = (
        "nombre",
        "novedad",
        "via_administrativa",
        "material",
        "instrucciones_almacenamiento",
        "instrucciones_uso",
    )  # Agrega los campos que deseas habilitar para la búsqueda
