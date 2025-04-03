"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importa el módulo de administración de Django.
from django.urls import path, include # Importa funciones para definir URLs.
from django.conf import settings  # Importa configuración del proyecto.
from django.conf.urls.static import static # Importa una función para servir archivos estáticos en desarrollo.

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta para el panel de administración.
    path('cart/', include('cart.urls', namespace='cart')), # Incluye las URLs de la app "cart" con el nombre 'cart'.
    path('orders/', include('orders.urls', namespace='orders')),  # Incluye las URLs de la app "orders" con el nombre 'orders'.
    path('', include('shop.urls', namespace='shop')), # Ruta principal que incluye las URLs de la app "shop" con el nombre 'shop'.
]

# Si el modo DEBUG está activado, añade las rutas para servir archivos estáticos (como imágenes).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)