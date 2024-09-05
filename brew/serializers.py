from rest_framework import serializers
from django.contrib.auth.models import User
import re
from .models import Coffee
from .models import Snack

class CoffeeSerializer(serializers.ModelSerializer):
    
    """Serializer for the coffee model. 
    
    Converts Coffee model instances into JSON format.

    Fields:
        id (int): A unique integer value identifying this coffee.
        coffee_name (str): The name or type of the coffee, e.g., 'Espresso', 'Latte'.
        temperature (str): The serving temperature of the coffee, e.g., 'Hot', 'Iced'.
        caffeine_amount (int): The amount of caffeine in milligrams.
        price (float): The price of the coffee in USD.
        description (str): A short description of the coffee.
        in_stock (bool): Whether or not the coffee is available for purchase.
    """
    
    id = serializers.CharField(help_text='A unique integer value identifying this coffee.')
    coffee_name = serializers.CharField(help_text='The type of coffee')
    temperature = serializers.CharField(help_text='The temperature of the coffee')
    caffeine_amount = serializers.IntegerField(help_text='The amount of caffeine in the coffee')
    price = serializers.FloatField(help_text='The price of the coffee in USD')
    description = serializers.CharField(help_text='A description of the coffee')
    in_stock = serializers.BooleanField(help_text='Whether or not the coffee is in stock')
    class Meta:
        model=Coffee
        fields=['id', 'coffee_name', 'temperature', 'caffeine_amount', 'price', 'description', 'in_stock']
        
class SnackSerializer(serializers.ModelSerializer):
    """Serializer for the snack model. 
    
    Converts Snack model instances into JSON format.

    Fields:
        id (int): The unique identifier for the snack.
        snack_name (str): The name of the snack, e.g. 'Muffin', 'Chips'        
        price (float): The price of the snack in USD.
        description (str): A short description of the snack.
        in_stock (bool): Whether or not the coffee is available for purchase.
    """
    
    id = serializers.CharField(help_text='The unique identifier for the snack')
    snack_name = serializers.CharField(help_text='The name of the snack')
    price = serializers.FloatField(help_text='The price of the snack in USD')
    description = serializers.CharField(help_text='A description of the snack')
    in_stock = serializers.BooleanField(help_text='Whether or not the snack is in stock')
    
    class Meta:
        model=Snack
        fields=['id', 'snack_name', 'price', 'description', 'in_stock']
    
class UserSignupSerializer(serializers.ModelSerializer):
    """Serializer for user signups. 
    
    Validates and creates a user account with a username and password.

    Fields:
        username (str): The user's username. Must be alphanumeric.
        password (str): The user's password. Must be alphanumeric.

    Raises:
        serializers.ValidationError: If the username or password is not alphanumeric.
        
    Methods:
        def_validate_username(username): Validates that username is alphanumeric. 
        def_validate_password(password): Validates that password is alphanumeric. 
        def_create: Creates a new user with validated data

    Returns:
        User: the new User instance
    """
    
    username = serializers.CharField(
        required=True,
        error_messages={
            "required": "A username is required.",
        }
    )
    password = serializers.CharField(
        required=True,
        error_messages={
            "required": "A password is required.",
        }
    )

    class Meta:
        model = User
        fields = ('username', 'password')
    
    def validate_username(self, username):
        if not re.match("^[a-zA-Z\\d]*$", username):
            raise serializers.ValidationError({"message": "Username can only contain letters and numbers."})
        return username

    def validate_password(self, password):
        if not re.match("^[a-zA-Z\\d]*$", password):
            raise serializers.ValidationError({"message": "Password can only contain letters and numbers."})      
        return password
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user