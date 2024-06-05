from django.db import models
from django.contrib.auth import get_user_model
from product.views import ProducstModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='order')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProducstModel, on_delete=models.SET_NULL, related_name='order', null=True)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=128)
    image1 = models.ImageField(upload_to="order")
    image2 = models.ImageField(upload_to="order")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items' 

