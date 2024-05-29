from django import forms

from pages.models import ContactModel


class ContactModelForm(forms.Form):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']