from django.urls import path
from .views import UserRegistrationView
from .views import PingView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('api/ping/', PingView.as_view(), name='ping')
]