from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignupView
from .views import PingView
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/ping/', PingView.as_view(), name='ping'),
    path('api/', include(router.urls)) 
]