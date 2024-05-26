from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    price = forms.DecimalField(label='price', max_digits=10, decimal_places=2)
    description = forms.CharField(label='description', max_length=100)
    category = forms.CharField(label='category', max_length=100)
    image = forms.ImageField(label='image')