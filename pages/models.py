from django.db import models

# Create your models her
class FormContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Form Contact"
        verbose_name_plural = "Form Contacts"
        
        
        
        
class FedbackModelPage(models.Model):
    fedbacks = models.TextField()
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Fedback"
        verbose_name_plural = "Fedbacks"