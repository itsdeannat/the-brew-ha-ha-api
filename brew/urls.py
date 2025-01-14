from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignupView
from .views import PingView
from .views import ProductViewSet
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')


urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/ping/', PingView.as_view(), name='ping'),
    path('api/', include(router.urls)) 
]