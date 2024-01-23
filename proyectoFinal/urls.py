from django.contrib import admin
from django.urls import path, include
from aplicacion.views import (
    InventarioViewSet,
    AlmacenViewSet,
    RolPersonaViewSet,
    PersonalViewSet,
    CategoriaProductoViewSet,
    ProductoViewSet
)
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()

# Registrar las vistas en el router
router.register(r'inventarios', InventarioViewSet, 'inventarios')
router.register(r'almacenes', AlmacenViewSet, 'almacenes')
router.register(r'rolpersonas', RolPersonaViewSet, 'rolpersonas')
router.register(r'personales', PersonalViewSet, 'personales')
router.register(r'categoriaproductos', CategoriaProductoViewSet, 'categoriaproductos')
router.register(r'productos', ProductoViewSet, 'productos')

# Para editar el endpoint de la API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

