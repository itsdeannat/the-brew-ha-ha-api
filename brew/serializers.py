from rest_framework import serializers
from django.contrib.auth.models import User
import re
from django.db import transaction
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
    temperature = serializers.CharField(help_text='Drink temperature', required=False)
    caffeine_amount = serializers.IntegerField(help_text="Caffeine amount in milligrams", required=False)
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
    """ 
    Serializer for the Order Item model.
    
    Converts Order Item model into JSON format.
    
    Fields:
        product_id (int): The ID of the product in the database
        product_name (str): The name of the product in the database
        quantity (int): The amount of product requested
    
    """
    product_id = serializers.IntegerField(source='product.id') 
    product_name = serializers.CharField(source='product.product_name', read_only=True) 
    quantity = serializers.IntegerField(source='product.product_quantity')

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity', 'product_name']


class OrderSerializer(serializers.ModelSerializer):
    """ 
    Serializer for the Order model
    
    Converts Order model to JSON format. 
    
    Fields:
        id (int): The unique ID for the order
        order_items (OrderItemSerializer): References the Order Item serializer and links order items to an order
        order_date (datetime): The date the order is submitted. Set to readonly to return to the customer
        status (str): The status of the order. Set to readonly to return to the customer
        payment_method (str): The payment method used
    """
    
    id = serializers.IntegerField(read_only=True, help_text="The unique order id")
    order_items = OrderItemSerializer(many=True, required=True, help_text="The items in the customer's order. Provide the `product_id` and quantity for each product.")  
    order_date = serializers.DateTimeField(read_only=True, help_text="Order date") 
    status = serializers.CharField(read_only=True, help_text="Order status") 
    payment_method = serializers.CharField(required=True, help_text="The payment method used")
    

    class Meta:
        model = Order
        fields = ['id', 'payment_method', 'order_date', 'status', 'order_items']
        
    
    '''
    Creates an order in the Brew Ha Ha database
    
    Parameters:
        order_data (dict): A dictionary containing the data for the order
        
    Returns:
        order: The newly created order with the order items
    '''
    def create(self, order_data):
        order_items_data = order_data.pop('order_items') 
        
        # Ensure transaction is successful before committing to the DB
        with transaction.atomic():  
            order = Order.objects.create(**order_data) 
            
            for order_item_data in order_items_data: 
                # Gets the product id for the order item
                product = Product.objects.get(id=order_item_data['product']['id']) 

                # Verify that the item is still in stock
                if order_item_data['quantity'] > product.quantity:
                    raise serializers.ValidationError(f"{product.product_name} is out of stock.")

                # Create the OrderItem
                OrderItem.objects.create(order=order, product=product, quantity=order_item_data['quantity'])

                # Update the product quantity 
                product.quantity -= order_item_data['quantity']
                product.save()
        
        return order
    
class BadRequestSerializer(serializers.Serializer):
    """
    Serializer for the 401 Unauthorized response
    """
    detail = serializers.CharField(default="The request body could not be read properly.")

class UnauthorizedSerializer(serializers.Serializer):
    """ 
    Serializer for 400 Bad Request responses
    """
    detail = serializers.CharField(default="Authentication credentials were not provided.")

class NotFoundSerializer(serializers.Serializer):
    """
    Serializer for the 404 Not Found responses
    """
    detail = serializers.CharField(default="The requested resource was not found.")    