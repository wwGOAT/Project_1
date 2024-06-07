from django.contrib import admin
from pages.models import FormContactModel, FedbackModelPage
# Register your models here.
@admin.register(FormContactModel)
class FormContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')
    
    
@admin.register(FedbackModelPage)
class FedbackModelPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'create_at')
    list_filter = ('name', 'position')
    search_fields = ('name', 'position')