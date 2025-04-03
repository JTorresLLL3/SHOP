from decimal import Decimal  # Importa Decimal para manejar precios con precisión decimal.
from django.conf import settings  # Importa la configuración de Django.
from shop.models import Product  # Importa el modelo Product de la tienda.


class Cart:
    def __init__(self, request):
        """
        Inicializa el carrito de compras.
        """
        self.session = request.session  # Obtiene la sesión del usuario.
        cart = self.session.get(settings.CART_SESSION_ID)  # Intenta obtener el carrito de la sesión.
        if not cart:
            # Si no hay carrito en la sesión, crea un carrito vacío.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart  # Guarda el carrito en la instancia de la clase.

    def __iter__(self):
        """
        Itera sobre los productos en el carrito y obtiene sus detalles desde la base de datos.
        """
        product_ids = self.cart.keys()  # Obtiene las claves (IDs de productos) del carrito.
        products = Product.objects.filter(id__in=product_ids)  # Busca los productos en la base de datos.
        cart = self.cart.copy()  # Hace una copia del carrito para trabajar con él.

        for product in products:
            cart[str(product.id)]['product'] = product  # Asocia cada producto con su objeto correspondiente.

        for item in cart.values():
            item['price'] = Decimal(item['price'])  # Convierte el precio en un número decimal.
            item['total_price'] = item['price'] * item['quantity']  # Calcula el precio total del producto en el carrito.
            yield item  # Devuelve cada producto con sus datos actualizados.

    def __len__(self):
        """
        Cuenta la cantidad total de productos en el carrito.
        """
        return sum(item['quantity'] for item in self.cart.values())  # Suma todas las cantidades de productos.

    def add(self, product, quantity=1, override_quantity=False):
        """
        Agrega un producto al carrito o actualiza su cantidad.
        """
        product_id = str(product.id)  # Convierte el ID del producto a string para usarlo como clave en el diccionario.
        if product_id not in self.cart:

            # Si el producto no está en el carrito, lo agrega con cantidad 0 y su precio como string.
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if override_quantity:

            # Si override_quantity es True, reemplaza la cantidad existente.
            self.cart[product_id]['quantity'] = quantity
        else:
            
            # Si no, suma la cantidad especificada a la existente.
            self.cart[product_id]['quantity'] += quantity

        self.save()  # Guarda los cambios en la sesión.

    def save(self):
        """
        Marca la sesión como modificada para asegurarse de que se guarde.
        """
        self.session.modified = True  # Indica que la sesión ha sido modificada.

    def remove(self, product):
        """
        Elimina un producto del carrito.
        """
        product_id = str(product.id)  # Obtiene el ID del producto como string.
        if product_id in self.cart:
            del self.cart[product_id]  # Elimina el producto del carrito.
            self.save()  # Guarda los cambios en la sesión.

    def clear(self):
        """
        Elimina el carrito de la sesión.
        """
        del self.session[settings.CART_SESSION_ID]  # Borra la información del carrito en la sesión.
        self.save()  # Guarda los cambios en la sesión.

    def get_total_price(self):
        """
        Calcula el precio total de todos los productos en el carrito.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
