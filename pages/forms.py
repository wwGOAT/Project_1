from django.forms import forms, ModelForm
from pages.models import FormContactModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class FormViewContact(ModelForm):
    models = FormContactModel
    fields = ['name', 'email', 'subject', 'message']
    class Meta:
        model = FormContactModel
        fields = ['name', 'email', 'subject', 'message']