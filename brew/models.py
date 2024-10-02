from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    """
    Model representing a product in the Brew Ha Ha database
    
    Attributes:
        product_name (str): The name of the product, e.g. 'Muffin', 'Espresso'
        temperature (str): The serving temperature for coffees, e.g. 'Hot', 'Iced'
        caffeine_amount (int): The amount of caffeine in milligrams
        price (float): The price of the product
        description (str): A short description of the product
        quantity (int): Amount of product available
    """    
    product_name = models.CharField(max_length=200, default='Default Description')
    temperature = models.CharField(max_length=500, blank=True, null=True)
    caffeine_amount = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=200, default='Default Description')  
    quantity = models.IntegerField(default=True)
    
class Order(models.Model):
    PAYMENT_METHODS = [ # Only choices customers can include in request
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default="in progress")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE) # Links orders to order items
    product = models.ForeignKey('Product', on_delete=models.CASCADE) # Links products to order items for matching
    quantity = models.PositiveIntegerField()