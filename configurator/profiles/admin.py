from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ('id', 'address', 'created_at', 'updated_at')

