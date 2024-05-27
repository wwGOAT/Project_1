from django.contrib import admin
from products.models import *


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'created_at',)
    list_filter = ('name', 'long_description', 'short_description', )
    search_fields = ('created_at', 'updated_at',)


@admin.register(ProductManufacture)
class ProductManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at',)


@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at',)


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at',)


@admin.register(ProductColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at',)