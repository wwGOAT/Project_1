from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

UserModel= get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = UserModel.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    
   
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, min_length=6)
    
    
    
class EmailVerificationForm(forms.Form):
   code_verfiy = forms.CharField(max_length=6)