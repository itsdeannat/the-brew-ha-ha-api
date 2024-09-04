from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignupView
from .views import PingView
from .views import CoffeeViewSet
from .views import SnackViewSet

router = DefaultRouter()
router.register(r'coffees', CoffeeViewSet, basename='coffee')
router.register(r'snacks', SnackViewSet, basename='snack')


urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/ping/', PingView.as_view(), name='ping'),
    path('api/', include(router.urls)) 
]