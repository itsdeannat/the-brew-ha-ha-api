from django.urls import path
from .views import UserSignupView
from .views import PingView
from .views import GetAllCoffeesView
from .views import GetAllSnacksView


urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/ping/', PingView.as_view(), name='ping'),
    path('api/coffees/', GetAllCoffeesView.as_view(), name='coffees'),
    path('api/snacks/', GetAllSnacksView.as_view(), name='snacks')
]