from django.contrib import admin
from blogs.models import BlogcategoryModle, BlogModel, AuthorModel, BlogTag


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at"]
    search_fields = ["name"]
    list_filter = ["name", "create_at"]
    
@admin.register(BlogcategoryModle)
class BlogcategoryModleAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at"]
    search_fields = ["name"]
    list_filter = ["name", "create_at"]
    
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["title", "create_at"]
    search_fields = ["title", "content"]
    list_filter = [ "create_at"]
    
@admin.register(BlogTag)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at"]
    search_fields = ["name"]
    list_filter = [ "create_at"]