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