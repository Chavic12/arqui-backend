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
router.register(r'inventarios', InventarioViewSet)
router.register(r'almacenes', AlmacenViewSet)
router.register(r'rolpersonas', RolPersonaViewSet)
router.register(r'personales', PersonalViewSet)
router.register(r'categoriaproductos', CategoriaProductoViewSet)
router.register(r'productos', ProductoViewSet)

# Para editar el endpoint de la API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()