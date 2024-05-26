from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=128),
    email = models.CharField(max_length=128),
    subject = models.CharField(max_length=128),
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

