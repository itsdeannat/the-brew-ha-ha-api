from django.db import models

# Create your models here.

class Coffee(models.Model):
    """
    Model representing a coffee.
    
    Attributes:
        coffee_type (str): The name or type of the coffee, e.g., 'Espresso', 'Latte'.
        temperature (str): The serving temperature of the coffee, e.g., 'Hot', 'Iced'.
        caffeine_amount (int): The amount of caffeine in milligrams.
        price (float): The price of the coffee in USD.
    """
    coffee_type = models.CharField(max_length=200)
    temperature = models.CharField(max_length=500)
    caffeine_amount = models.IntegerField()
    price = models.FloatField()

class Snack(models.Model):
    """
    Model representing a snack.
    
    Attributes:
        coffee_type (str): The name or type of the snack, e.g., 'Chips', 'Muffin'.
        price (float): The price of the coffee in USD.
    """
    snack_name = models.CharField(max_length=200, null=True)
    price = models.FloatField()