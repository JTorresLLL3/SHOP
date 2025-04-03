"""
Esta sección del código configura la interfaz de administración para Category y Product.  
- CategoryAdmin: Muestra nombre y slug, generando el slug automáticamente.  
- ProductAdmin: Muestra detalles clave, permite edición en línea y filtra por disponibilidad y fecha.  

"""

from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}