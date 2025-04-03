from .cart import Cart  # Trae la clase Cart del archivo cart.py en la misma carpeta.


def cart(request):
    """
    Esta función hace que el carrito esté disponible en todas las páginas.
    request: contiene datos de la sesión del usuario.
    """
    return {'cart': Cart(request)} # Devuelve: un objeto carrito que cualquier template puede usar.