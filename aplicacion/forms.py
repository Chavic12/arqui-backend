from django import forms
from .models import (
    Inventario,
    Almacen,
    RolPersona,
    Personal,
    CategoriaProducto,
    Producto,
)


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = "__all__"


class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = "__all__"


class RolPersonaForm(forms.ModelForm):
    class Meta:
        model = RolPersona
        fields = "__all__"


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = "__all__"


class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProducto
        fields = "__all__"


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
