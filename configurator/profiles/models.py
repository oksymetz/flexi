from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Primary Key
    name = models.CharField(max_length=255)          # Name field
    email = models.EmailField(unique=True)           # Email field with uniqueness constraint
    address = models.TextField()                     # Address field for longer text
    password_hash = models.CharField(max_length=255) # Password hash field
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)     # Automatically update on modification

    def __str__(self):
        return self.name