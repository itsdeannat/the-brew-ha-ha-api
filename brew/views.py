from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Coffee
from .models import Snack
from .serializers import CoffeeSerializer, SnackSerializer, UserSignupSerializer

# Create your views here.
class GetAllCoffeesView(APIView):
        
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        request=None,
        responses={
            200: CoffeeSerializer(many=True),
        },
        examples=[
            OpenApiExample(
                name="Example coffee details",
                description="",
                value={
                    "id": 1,
                    "type": "mocha",
                    "temperature": "hot",
                    "caffeine_amount": 105,
                    "price": 3.75
                },
                response_only=True
            ),
        ],
        methods=['GET'],
        description="Get all coffees in the inventory. The response includes information about each coffee's type, temperature, caffeine amount, and price."
    )
    def get(self, request):
        coffee = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee, many=True)
        return Response(serializer.data)
    
class GetAllSnacksView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema( 
        request=None,
        responses={
            200: SnackSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example snack details",
                description="",
                value={
                    "id": 1,
                    "snack_name": "muffin", 
                    "price": 3.00
                },
                response_only=True
            ),
        ],
        methods=['GET'],        
        description="Gets all snacks in the inventory. The response includes information about each snack's name and price."
    )            
    def get(self, request):
        snack = Snack.objects.all()
        serializer = SnackSerializer(snack, many=True)
        return Response(serializer.data)
    
class UserSignupView(APIView):

    @extend_schema(exclude=True)
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Signup successful!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(exclude=True)
    def get(self, request, format=None):
        content = {
            "message": "Test ping successful!"
        }
        return Response(content, status=status.HTTP_200_OK)