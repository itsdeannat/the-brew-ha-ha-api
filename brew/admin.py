from django.contrib import admin

# Register your models here.
from .models import Coffee  
from .models import Snack

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('coffee_type', 'temperature', 'caffeine_amount', 'price')  
    
@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ('snack_name', 'price')
