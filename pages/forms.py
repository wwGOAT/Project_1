from django import forms
from pages.models import ContactModel
from django.contrib.auth import get_user_model
user_model = get_user_model()


class ContactModelForm(forms.Form):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']