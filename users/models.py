from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your models here.
class VerficationCodeModel(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="verfication_code")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "VerficationCode"
        verbose_name_plural = "VerficationCodes"

class AccountModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="account")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"