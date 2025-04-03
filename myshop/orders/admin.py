from django.contrib import admin
from .models import Order, OrderItem  # Importa los modelos Order y OrderItem del mismo directorio.

# Clase para mostrar OrderItem como inline en la interfaz de administración.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product'] # Muestra un campo de búsqueda para productos.


# Registra y configura el modelo Order en el admin.
@admin.register(Order)

# Clase que configura cómo se muestra Order en admin.
class OrderAdmin(admin.ModelAdmin):

    # Campos que se mostrarán en la lista de órdenes.
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    
    # Filtros que aparecerán en el sidebar derecho.
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline] # Incluye los OrderItems relacionados.