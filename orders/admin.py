from django.contrib import admin
from orders.models import OrderModel, OrderItemModel

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')


@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'size')
    search_fields = ('product_name',)


