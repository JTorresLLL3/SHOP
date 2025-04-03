from django.urls import path  # Importa la función path para definir las rutas.
from . import views  # Importa las vistas del mismo directorio.

app_name = 'cart'  # Define un espacio de nombres para las rutas de la aplicación "cart".

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'), # Ruta para ver el carrito de compras.
    path('add/<int:product_id>/', views.cart_add, name='cart_add'), # Ruta para agregar un producto al carrito, recibe el ID del producto.
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'), # Ruta para eliminar un producto del carrito, recibe el ID del producto.  
]
