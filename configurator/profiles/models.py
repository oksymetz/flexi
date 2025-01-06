from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()                     # Address field for longer text
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)     # Automatically update on modification
