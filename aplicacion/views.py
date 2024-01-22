from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .forms import *
from aplicacion.models import (
    Inventario,
    Almacen,
    RolPersona,
    Personal,
    CategoriaProducto,
    Producto,
)
from aplicacion.serializers import (
    InventarioSerializer,
    AlmacenSerializer,
    RolPersonaSerializer,
    PersonalSerializer,
    CategoriaProductoSerializer,
    ProductoSerializer,
)

# Create your views here.


def index(request):
    return render(request, 'index.html')


def crearProducto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ProductoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_Producto.html', diccionario)


def bsuquedadStock(request):
    producto = Producto.objects.all()
    insumos = 0
    medicamentos = 0
    dispositivos = 0
    for e in producto:
        if (e.categoria.nombre == "Dispositivos Medicos"):
            dispositivos += 1
        if (e.categoria.nombre == "Insumos Medicos"):
            insumos += 1
        if (e.categoria.nombre == "Medicamentos"):
            medicamentos += 1
    informacion_template = {'insumos': insumos, 'medicamentos': medicamentos,
                            'dispositivos': dispositivos, 'productos': producto}
    return render(request, 'stock.html', informacion_template)


def RegistraProducto(request):
    pass


def devuelveExistenciaProducto(request):
    pass


def actualizaStock(request):
    pass


def devuelveDetallesProducto(request):
    pass


def devuelveDetallesNovedades(request):
    pass


def registrarMotivoRetiro(request):
    pass


def devuelveDetallesProductoEmpacado(request):
    pass


def devuelveDetallesLlegada(request):
    pass


########################################################

# Almacen


def notificaLlegada():
    pass


# Operador
def seleccionaProductoEmpacar():
    pass


def transportarProducto():
    pass


def registrarLlegadaProdcuto():
    pass


# Jefe


def empacaProducto():
    pass


def seleccionarProducto():
    pass


def despacharProcuto():
    pass


def asignarUbicacion():
    pass


# Gestor


def verificarDetalleProducto():
    pass


def retirarProductoMalE():
    pass


################################################
# API REST


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer


class RolPersonaViewSet(viewsets.ModelViewSet):
    queryset = RolPersona.objects.all()
    serializer_class = RolPersonaSerializer


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
