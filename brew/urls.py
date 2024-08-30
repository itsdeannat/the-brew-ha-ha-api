from django.urls import path
from .views import UserRegistrationView
from .views import PingView


urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/ping/', PingView.as_view(), name='ping')
]