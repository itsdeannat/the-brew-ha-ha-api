from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Coffee
from .models import Snack
from .serializers import CoffeeSerializer, SnackSerializer, UserSignupSerializer

# Create your views here.

class CoffeeViewSet(ReadOnlyModelViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = CoffeeSerializer
    queryset = Coffee.objects.all()
    
    @extend_schema(
        operation_id="list_coffees",
        description="Returns a list of all coffee objects in the database",
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
        },
        examples=[
            OpenApiExample(
                name="Successful Response",
                description="",
                value={
                    "results": [
                        {
                            "id": 1,
                            "type": "mocha",
                            "temperature": "hot",
                            "caffeine_amount": 105,
                            "price": 3.75
                        },
                        {
                            "id": "2",
                            "coffee_type": "latte",
                            "temperature": "hot",
                             "caffeine_amount": 95,
                            "price": 2.5
                        },
                        {
                            "id": "3",
                            "coffee_type": "cortado",
                            "temperature": "hot",
                            "caffeine_amount": 130,
                            "price": 4.0
                        }
                    ]
                },
                response_only=True,
                status_codes=["200"]
            ),
            OpenApiExample(
                name="Bad Request",
                description="",
                value={"detail": "The request body could not be read properly."},
                response_only=True,
                status_codes=["400"],
            ),
            OpenApiExample(
                name="Unauthorized",
                description="",
                value={"detail": "Authentication credentials were not provided."},
                response_only=True,
                status_codes=["401"],
            ),
            OpenApiExample(
                name="Not Found",
                description="",
                value={"detail": "No Coffee matches the given query."},
                response_only=True,
                status_codes=["404"],
            ),
        ],
    )
    def list(self, request):
        queryset = Coffee.objects.all()
        serializer = CoffeeSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        operation_id="retrieve_coffee",
        description="Returns a single coffee object based on its ID",
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
                    "caffeine_amount": 105,
                    "price": 3.75
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
            value={"detail":"No Coffee matches the given query."},
            response_only=True,
            status_codes=["404"],
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        queryset = Coffee.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CoffeeSerializer(user)
        return Response(serializer.data)
    

class SnackViewSet(ReadOnlyModelViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = SnackSerializer
    queryset = Snack.objects.all()
    
    @extend_schema(
        operation_id="list_snacks",
        description="Returns a list of all snack objects in the database",
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT
        },
        examples=[
            OpenApiExample(
                name="Example snack details",
                description="",
                value={
                    "results": [
                        {
                            "id": 1,
                            "snack_type": "muffin",
                            "price": 3.00
                        },
                        {
                            "id": 2,
                            "snack_type": "bagel",
                            "price": 1.50
                        },
                        {
                            "id": 3,
                            "snack_type": "croissant",
                            "price": 2.00
                        }
                    ]
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
    )
    def list(self, request):
        queryset = Snack.objects.all()
        serializer = SnackSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        operation_id="retrieve_snack",
        description="Returns a single snack object based on its ID",
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
                    "id": 3,
                    "product_name": "croissant", 
                    "price": 2.00
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
    )
    def retrieve(self, request, pk=None):
        queryset = Snack.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SnackSerializer(user)
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