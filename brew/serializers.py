from rest_framework import serializers
from django.contrib.auth.models import User
import re

class UserSignupSerializer(serializers.ModelSerializer):
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