from django.urls import path
from .views import RegisterView,  LoginView, verfiy_email_code_check

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user-register.html', RegisterView.as_view(), name='user_register'),
    path('email/verfiy/', verfiy_email_code_check, name="email")
]                                   