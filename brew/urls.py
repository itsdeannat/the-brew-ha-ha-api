from django.urls import path
from .views import UserSignupView
from .views import PingView


urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/ping/', PingView.as_view(), name='ping')
]