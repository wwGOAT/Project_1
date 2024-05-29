# pages/admin.py
from django.contrib import admin
from .models import ContactModel

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at',)
    list_filter = ('email', 'created_at',)
    search_fields = ('name', 'email', 'subject', 'created_at',)
