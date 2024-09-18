from django.db import models

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
        in_stock (bool): Whether the product is in stock
    """    
    product_name = models.CharField(max_length=200, default='Default Description')
    temperature = models.CharField(max_length=500, blank=True, null=True)
    caffeine_amount = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=200, default='Default Description')    
    in_stock = models.BooleanField(default=True)