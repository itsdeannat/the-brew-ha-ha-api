from django.contrib import admin

# Register your models here.
from .models import Product 
from .models import Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'temperature', 'caffeine_amount', 'price', 'description', 'quantity')  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('payment_method', 'order_date', 'status')