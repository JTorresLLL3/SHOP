from django import forms # Importa el módulo de formularios de Django.
from .models import Order # Importa el modelo Order desde el archivo models.py en la misma carpeta.


# Define un formulario basado en el modelo Order.
class OrderCreateForm(forms.ModelForm):
    class Meta:

        # Se especifica que este formulario está basado en el modelo Order,
        model = Order

        # Lista los campos que aparecerán en el formulario.
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']