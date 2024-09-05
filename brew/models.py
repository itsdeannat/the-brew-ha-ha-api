from django.db import models

# Create your models here.

class Coffee(models.Model):
    """
    Model representing a coffee.
    
    Attributes:
        coffee_name (str): The name of the coffee, e.g., 'Espresso', 'Latte'.
        temperature (str): The serving temperature of the coffee, e.g., 'Hot', 'Iced'.
        caffeine_amount (int): The amount of caffeine in milligrams.
        price (float): The price of the coffee in USD.   
        description (str): A short description of the coffee.             
        in_stock (bool: Whether or not the coffee is available for purchase.
    """
    coffee_name = models.CharField(max_length=200, default='Default Description')
    temperature = models.CharField(max_length=500)
    caffeine_amount = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=200, default='Default Description')    
    in_stock = models.BooleanField(default=True)

class Snack(models.Model):
    """
    Model representing a snack.
    
    Attributes:
        snack_name (str): The type of snack, e.g., 'Chips', 'Muffin'.
        price (float): The price of the snack in USD.
        description (str): A short description of the snack.  
        in_stock (bool): Whether or not the snack is available for purchase.
    """
    snack_name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=200, default='Default Description')
    in_stock = models.BooleanField(default=True)
    