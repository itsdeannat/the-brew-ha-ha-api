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
    """
    Model representing an order in the Brew Ha Ha detabase

    Attributes:
        payment_method (str): Accepted payment choices, e.g. 'Credit', 'Debit')
        order_date (str): The date the order is submitted
        status (str): The status of the order, e.g. 'in progress', 'canceled', 'completed'
    """
    payment_methods = [ 
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    
    payment_method = models.CharField(max_length=20, choices=payment_methods)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default="in progress")

class OrderItem(models.Model):
    """Model for order items in the Brew Ha Ha database

    Attributes:
        order (ForeignKey): References the Order model and links orders to order items
        Product (ForeignKey): References the Product model and links products to order items for matching
        quantity (PositiveIntegerField): The amount of product in stock
    """
    # Because an order can have multiple items but an item can only be in one order
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    # Because a product can appear in multiple order items but an order item is associated with 1 product only
    product = models.ForeignKey('Product', on_delete=models.CASCADE) 
    # Make sure stock quantity is zero or above
    quantity = models.PositiveIntegerField()