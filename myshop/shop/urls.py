"""
Configuración de URLs para la aplicación 'shop':
- Define las rutas para las vistas de la tienda.
- Mapea URLs a funciones de vista con nombres únicos.
- Incluye patrones para listar productos, filtrar por categoría y ver detalles.
"""

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('mapa/', views.mapa, name='mapa'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]