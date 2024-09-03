from django.urls import path
from .views import UserSignupView
from .views import PingView
from .views import GetAllCoffeesView
from .views import GetAllSnacksView
from .views import GetCoffeeByIdView
from .views import GetSnackByIdView


urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/ping/', PingView.as_view(), name='ping'),
    path('api/coffees/', GetAllCoffeesView.as_view(), name='get_all_coffees'),
    path('api/snacks/', GetAllSnacksView.as_view(), name='get_all_snacks'),
    path('api/coffees/<int:pk>/', GetCoffeeByIdView.as_view(), name='get_coffee_by_id'),
    path('api/snacks/<int:pk>', GetSnackByIdView.as_view(), name='get_snack_by_id')    
]