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
    class Meta:
        model = Almacen
        fields = "__all__"


class RolPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPersona
        fields = "__all__"


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = "__all__"


class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    inventario = InventarioSerializer()
    categoriaProducto = CategoriaProductoSerializer()
    class Meta:
        model = Producto
        fields = "__all__"
