"""
-Este código define dos modelos de base de datos: 'Category' y 'Product', esenciales para gestionar nuestro e-commerce.
-'Category' representa las categorías de productos con un nombre y un identificador único ('slug'), proporcionando métodos como 'get_absolute_url' para navegar entre categorías.
-'Product' representa los productos individuales, vinculados a una categoría a través de una relación ('ForeignKey') y 
  almacenando información como nombre, descripción, precio, disponibilidad e imágenes.
-Además, ambos modelos incluyen configuraciones de metadatos para ordenar registros, crear índices que optimizan búsquedas, y métodos personalizados como '__str__' y 'get_absolute_url' para facilitar la interacción con los datos.

"""

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])