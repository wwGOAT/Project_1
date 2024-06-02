from django.contrib import admin
from .models import ProducstModel, ProductTagModel, ProducuctsChoisSizeModel, ManufactureProductsModel, ColorProducstModel, CategoryProductsModel, CommentsProductsModle# Register your models here.
@admin.register(ProducstModel)
class ProducstModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    search_fields = ["title", "created_at"]
    
    

@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name", "created_at"]
    

@admin.register(ProducuctsChoisSizeModel)
class ProducuctsChoisSizeModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name", "created_at"]
    

@admin.register(ManufactureProductsModel)
class ManufactureProductsModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name", "created_at"]
    

@admin.register(ColorProducstModel)
class ColorProducstModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name", "created_at"]
    

@admin.register(CategoryProductsModel)
class CategoryProductsModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name", "created_at"]
    
    
@admin.register(CommentsProductsModle)
class CommentsModleAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created_at', 'updated_at']
