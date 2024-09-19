from django.contrib import admin

# Register your models here.
from .models import Product 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'temperature', 'caffeine_amount', 'price', 'description', 'quantity')  

