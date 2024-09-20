from rest_framework import serializers
from django.contrib.auth.models import User
import re
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the product model. 
    
    Converts Product model instances into JSON format.
    
    Fields:
        id (int): A unique integer value identifying this product.
        product_name (str): The name of the product, e.g. 'Muffin', 'Espresso'
        temperature (str): The serving temperature for coffees, e.g. 'Hot', 'Iced'
        caffeine_amount (int): The amount of caffeine in milligrams.
        price (float): The price of the product in USD.
        description (str): A short description of the product.
        quantity (int): Amount of product available
    """
    id = serializers.IntegerField(help_text='A unique integer value identifying this product.')
    product_name = serializers.CharField(help_text='The product name')
    temperature = serializers.CharField(help_text='The temperature of the coffee', required=False)
    caffeine_amount = serializers.IntegerField(help_text='The amount of caffeine in the coffee', required=False)
    price = serializers.FloatField(help_text='The price of the product in USD')
    description = serializers.CharField(help_text='A description of the product')
    quantity = serializers.IntegerField(help_text='Amount of product available')
    
    class Meta:
        model=Product
        fields = fields=['id', 'product_name', 'temperature', 'caffeine_amount', 'price', 'description', 'quantity']

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
    
class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id') # Will populate this field with the product's id from the DB
    product_name = serializers.CharField(source='product.product_name', read_only=True) # Will populate this field with the product's name 

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity', 'product_name']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)  
    order_date = serializers.DateTimeField(read_only=True) # Set to readonly to return to the customer
    status = serializers.CharField(read_only=True) # Set to readonly to return to the customer

    class Meta:
        model = Order
        fields = ['payment_method', 'order_date', 'status', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items') # Gets the order items from customer's order
        order = Order.objects.create(**validated_data) # Creates a new order with the data 
        
        for order_item_data in order_items_data:
            # Fetch the product instance using the product_id
            product = Product.objects.get(id=order_item_data['product']['id'])
            # Create the OrderItem with the actual product instance
            OrderItem.objects.create(order=order, product=product, quantity=order_item_data['quantity']) # Create an Order Item
        
        return order