from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)] # Crea una lista de opciones para cantidades de productos del 1 al 20.


class CartAddProductForm(forms.Form): # Define un formulario para agregar productos al carrito.
    quantity = forms.TypedChoiceField( # Campo para seleccionar la cantidad de productos usando una lista de opciones.
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int) # Convierte el valor seleccionado en un entero.
    
    # Campo oculto que permite decidir si se sobrescribe la cantidad en el carrito.
    override = forms.BooleanField(required=False, # Es opcional.
                                  initial=False,  # Tiene un valor inicial de 'False'.
                                  widget=forms.HiddenInput) # El campo no se muestra en el formulario.