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
        operation_id="get_all_coffees",
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
    
class GetCoffeeByIdView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        operation_id="get_coffee_by_id",
        request=CoffeeSerializer,
        responses={
            200: CoffeeSerializer,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
        },
        examples=[
            OpenApiExample(
                name="Example coffee details",
                description="",
                value={
                    "id": 1,
                    "type": "mocha",
                    "temperature": "hot",
                    "caffeine_amount": "105",
                    "price": "3.75"
                },
                response_only=True
            ),
            OpenApiExample(
            name="Bad Request",
            description="",
            value={"detail": "The request body could not be read properly"},  
            response_only=True,
            status_codes=["400"],
            ),
            OpenApiExample(
            name="Unauthorized",
            description="",
            value={"detail":"Authentication credentials were not provided."},
            response_only=True,
            status_codes=["401"],
            ),
            OpenApiExample(
            name="Not Found",
            description="",
            value={"detail":"No Coffee matches the given query."},
            response_only=True,
            status_codes=["404"],
            ),
        ],
        methods=['GET'],
        description="Get a coffee by ID. The response includes information about the coffee type, temperature, caffeine amount, and price for the coffee."
    )
    def get(self, request, pk):
        coffee = get_object_or_404(Coffee, pk=pk)
        serializer = CoffeeSerializer(coffee)
        return Response(serializer.data)
    
class GetAllSnacksView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema( 
        operation_id="get_all_snacks",
        request=None,
        responses={
            200: SnackSerializer,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
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
            OpenApiExample(
            name="Bad Request",
            description="",
            value={"detail": "The request body could not be read properly."
            },  
            response_only=True,
            status_codes=["400"],
            ),
            OpenApiExample(
            name="Unauthorized",
            description="",
            value={"detail":"Authentication credentials were not provided."},
            response_only=True,
            status_codes=["401"],
            ),
            OpenApiExample(
            name="Not Found",
            description="",
            value={"detail":"No Snack matches the given query."},
            response_only=True,
            status_codes=["404"],
            ),
        ],
        methods=['GET'],        
        description="Gets all snacks in the inventory. The response includes information about each snack's name and price."
    )            
    def get(self, request):
        snack = Snack.objects.all()
        serializer = SnackSerializer(snack, many=True)
        return Response(serializer.data)
    

class GetSnackByIdView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(  
        operation_id="get_snack_by_id",
        request=SnackSerializer,
        responses={
            200: SnackSerializer,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
        },
        examples=[
            OpenApiExample(
                name="Example snack details",
                description="",
                value={
                    "id": 1,
                    "product_name": "muffin", 
                    "price": 3.00
                },
                response_only=True
            ),
            OpenApiExample(
            name="Bad Request",
            description="",
            value={"detail": "The request body could not be read properly."
            },  
            response_only=True,
            status_codes=["400"],
            ),
            OpenApiExample(
            name="Unauthorized",
            description="",
            value={"detail":"Authentication credentials were not provided."},
            response_only=True,
            status_codes=["401"],
            ),
            OpenApiExample(
            name="Not Found",
            description="",
            value={"detail":"No Snack matches the given query."},
            response_only=True,
            status_codes=["404"],
            ),
        ],
        methods=['GET'],
        description="Get a snack by ID. The response includes information about the snack type, the brand name, and price.",
    )
    def get(self, request, pk):
        snack = get_object_or_404(Snack, pk=pk)
        serializer = SnackSerializer(snack)
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