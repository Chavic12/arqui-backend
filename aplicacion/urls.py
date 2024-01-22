from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear/producto', views.crearProducto, name='crear_producto'),
    path('stock', views.bsuquedadStock, name='stock')
]
