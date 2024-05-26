from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='message', max_length=155)