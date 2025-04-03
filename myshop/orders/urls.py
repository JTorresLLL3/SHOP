"""
# Este archivo define las rutas (URLs) relacionadas con los pedidos en la aplicación.
"""

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'), # URL para crear un pedido.
]