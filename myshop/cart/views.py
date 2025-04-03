from django.shortcuts import render, redirect, get_object_or_404 # Importa funciones para renderizar templates, redireccionar y obtener objetos.
from django.views.decorators.http import require_POST # Decorador para restringir vistas solo a peticiones POST.
from shop.models import Product # Importa el modelo Product de la aplicación shop (para los productos).
from .cart import Cart # Importa la clase Cart del archivo cart.py en el mismo directorio.
from .forms import CartAddProductForm # Importa el formulario para agregar productos al carrito.

# Vista para agregar productos al carrito.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request) # Inicializa el carrito usando la sesión del usuario.
    product = get_object_or_404(Product, id=product_id)  # Obtiene el producto o devuelve 404 si no existe.
    form = CartAddProductForm(request.POST) # Crea el formulario con los datos POST.
    if form.is_valid():
        cd = form.cleaned_data # Obtiene los datos limpios del formulario.
        cart.add(product=product, # Agrega el producto al carrito con cantidad y opción de override.
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail') # Redirecciona a la vista de detalle del carrito.

# Vista para eliminar productos del carrito.
@require_POST
def cart_remove(request, product_id):
    cart = Cart(request) # Inicializa el carrito usando la sesión del usuario.
    product = get_object_or_404(Product, id=product_id) # Obtiene el producto o devuelve 404 si no existe.
    cart.remove(product) # Elimina el producto del carrito.
    return redirect('cart:cart_detail')# Redirecciona a la vista de detalle del carrito.

# Vista para mostrar los detalles del carrito de compras.
def cart_detail(request):
    cart = Cart(request) # Inicializa el carrito usando la sesión del usuario.
    for item in cart: # Para cada item en el carrito, agrega un formulario de actualización.
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'cart/detail.html', {'cart': cart}) # Renderiza la plantilla con el contexto del carrito.