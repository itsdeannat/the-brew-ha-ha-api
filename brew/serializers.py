from rest_framework import serializers
from django.contrib.auth.models import User
import re

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        error_messages={
            "required": "An email is required.",
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
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    def validate_email(self, email):
        # Check to make sure email format is valid
        if not re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\\.[A-Z|a-z]{2,})+", email):
            raise serializers.ValidationError("Email format is invalid.")

    def validate_last_name(self, password):
        if not re.match("^[a-zA-Z\\d]*$", password):
            raise serializers.ValidationError("Password can only contain letters and numbers.")