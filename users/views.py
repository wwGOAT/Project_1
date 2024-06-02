from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import  redirect, render
from django.views.generic import FormView, CreateView
from .forms import RegisterForm, LoginForm, EmailVerificationForm
from django.contrib import messages
from random import randint
from .models import VerficationCodeModel
from django.core.mail import send_mail
from conf import settings
from datetime import datetime
import pytz
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

UserModel = get_user_model()
def send_code_email(user):
    random_code = randint(100000, 999999)
    
    if VerficationCodeModel.objects.filter(code=random_code).exists():
        send_code_email(user)
    else:
        VerficationCodeModel.objects.create(
            code=random_code, user=user
            )
        try:
            send_mail(
            'Verfication code',
            f'Verfication code: {random_code}',
            settings.EMAIL_HOST_USER,
            [user.email]
            )
            return True
        except Exception as e:
            print(e)
            return False
        
    
    

class RegisterView(CreateView):
    template_name = 'user-register.html'
    form_class =  RegisterForm
    
    success_url = '/email/verfiy/'
    
    def form_valid(self, form: BaseModelForm):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_code_email(user)
        return super().form_valid(form)
    
    
    def form_invalid(self, form: BaseModelForm):
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form= form))
    
    
def verfiy_email_code_check(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            code = form.clean_data['code']
            user =  VerficationCodeModel.objects.filter(code=code).first()
            if user:
                now = datetime.now(pytz.timezone(settings.TIME_ZONE))
                sent_time = user.created_at.astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(minuts=20)
                if sent_time > now:
                  user = UserModel.objects.filter(pk=user.pk).first()
                  if user:
                      user.is_active = True
                      user.save()
                  return redirect("pages:home")
                else:
                    messages.error(request, 'Code expired')
            else:
                messages.error(request, 'Code invalid')
        else:
            messages.error(request, form.errors)
            print(form.errors)
    return render(request, 'email-verfiy.html')


class LoginView(FormView):
    template_name = 'user-login.html'
    form_class = LoginForm
    success_url = reverse_lazy('pages:home')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            messages.error(self.request, 'username or password invalid')
            
    def form_invalid(self, form):
        print(form.errors)