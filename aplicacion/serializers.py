from rest_framework import serializers
from .models import (
    Inventario,
    Almacen,
    RolPersona,
    Personal,
    CategoriaProducto,
    Producto,
)


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"


class AlmacenSerializer(serializers.ModelSerializer):
    inventario_inventario = InventarioSerializer()

    class Meta:
        model = Almacen
        fields = "__all__"


class RolPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPersona
        fields = "__all__"


class PersonalSerializer(serializers.ModelSerializer):
    rol_rol = RolPersonaSerializer()
    inventario_inventario = InventarioSerializer()

    class Meta:
        model = Personal
        fields = "__all__"


class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    inventario_inventario = InventarioSerializer()
    categoria_categoria = CategoriaProductoSerializer()

    class Meta:
        model = Producto
        fields = "__all__"
