from django.urls import path
from .views import UserRegistrationView

url_patterns = [
     path('register/', UserRegistrationView.as_view(), name='user_registration'),
]