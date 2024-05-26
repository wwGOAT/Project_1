from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128),
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=128)
    image = models.ImageField(upload_to='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
