from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiRequest
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product, Order
from .serializers import ProductSerializer, UserSignupSerializer, OrderSerializer, BadRequestSerializer, UnauthorizedSerializer, NotFoundSerializer

# Create your views here.

class ProductViewSet(ReadOnlyModelViewSet):
    """ 
    View to get products from the Brew Ha Ha database
    """
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = None 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    @extend_schema(
        operation_id="retrieve_products",
        description="Returns a single product from the database",
        responses={
            200: ProductSerializer,
            400: BadRequestSerializer,
            401: UnauthorizedSerializer,
            404: NotFoundSerializer
        },
        examples=[
            OpenApiExample(
                name="Successful Response",
                description="",
                value=[
                    {
                        "id": 1,                 
                        "product_name": "mocha",           
                        "temperature": "hot",
                        "caffeine_amount": 105,
                        "price": 3.75,
                        "description": "A rich, decadent blend of espresso and chocolate",
                        "quantity": 8
                    },
                ],
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
                value={"detail": "No product matches the given query."},
                response_only=True,
                status_codes=["404"],
            ),
        ]
    )    
    def retrieve(self, request, pk=None):
        """ 
        Handles GET requests to get a specific product
        """
        queryset = Product.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(user)
        return Response(serializer.data)
    
    @extend_schema(
        operation_id="list_products",
        description="Returns a list of all products in the database",
        responses={
            200: ProductSerializer,
            400: BadRequestSerializer,
            401: UnauthorizedSerializer,
            404: NotFoundSerializer
        },
        examples=[
            OpenApiExample(
                name="Successful Response",
                description="",
                value=[
                        {
                            "id": 1,                 
                            "product_name": "mocha",           
                            "temperature": "hot",
                            "caffeine_amount": 105,
                            "price": 3.75,
                            "description": "A rich, decadent blend of espresso and chocolate",
                            "quantity": 8
                        },
                        {
                            "id": 2,                 
                            "product_name": "muffin",
                            "price": 2.50,
                            "description": "A fluffy, warm blueberry muffin",
                            "quantity": 5
                        },
                        {
                            "id": 3,                 
                            "product_name": "cortado",
                            "temperature": "hot",
                            "caffeine_amount": 130,
                            "price": 4.0,
                            "description": "Made with beans picked from the coast of Spain",
                            "quantity": 5
                        }
                    ],
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
                value={"detail": "No product matches the given query."},
                response_only=True,
                status_codes=["404"],
            ),
        ]
    )  
    def list(self, request):
        """
        Handles GET requests to get all products in the database
        """
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class UserSignupView(APIView):

    @extend_schema(exclude=True)
    def post(self, request):
        """
        Handles POST requests to create a new user in the database
        """
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
        """ 
        Handles GET requests to send a test ping to the server
        """
        content = {
            "message": "Test ping successful!"
        }
        return Response(content, status=status.HTTP_200_OK)
    
class OrderViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    View to create and get orders from the Brew Ha Ha database
    """
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    @extend_schema(
        operation_id="retrieve_orders",
        description="Returns a single order from the database",
        responses={
            200: OrderSerializer,
            400: BadRequestSerializer,
            401: UnauthorizedSerializer,
            404: NotFoundSerializer
        },
        examples=[
            OpenApiExample(
                name="Successful Response",
                description="",
                value=[
                    {
                        "id": "13",
                        "payment_method": "Credit",
                        "order_date": "2025-01-11T03:17:47.746025Z",
                        "status": "in progress",
                        "order_items": [
                            {
                                "product_id": 2,
                                "quantity": 1
                            }
                        ]
                    },
                ],
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
                value={"detail": "No product matches the given query."},
                response_only=True,
                status_codes=["404"],
            ),
        ]
    )
    def retrieve(self, request, pk=None):
        """
        Handles GET requests to get a specific order from the database
        """
        queryset = Order.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(user)
        return Response(serializer.data)  
    
    @extend_schema(
        operation_id="create_order",
        description="Order available products from the database",
        responses={
            201: OrderSerializer,
            400: BadRequestSerializer,
            401: UnauthorizedSerializer,
            404: NotFoundSerializer
        },
        examples=[
            OpenApiExample(
            name="Example Request",
            description="Example of a request to create an order",
            value={
                "payment_method": "Credit",
                "order_items": [
                    {
                        "product_id": 2,
                        "quantity": 1,
                    }
                ]
            },
            request_only=True,  # Indicates this is for the request
        ),
            OpenApiExample(
                name="Example response",
                description="",
                value=[
                    {
                        "id": 13,
                        "payment_method": "Credit",
                        "order_date": "2025-01-11T03:17:47.746025Z",
                        "status": "in progress",
                        "order_items": [
                            {
                                "product_id": 2,
                                "quantity": 1,
                            }
                        ]
                    },
                ],
                status_codes=["201"],
                response_only=True
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
                value={"detail": "The requested resource was not found"},
                response_only=True,
                status_codes=["404"]
            )
        ]
    )  
    def create(self, request, *args, **kwargs):
        """
        Handles POST requests to create an order in the Brew Ha Ha database
        """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    