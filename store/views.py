from django.shortcuts import redirect
from store.models import Category, Subcategory, Product,Restaurant  
from rest_framework import generics, permissions,filters
from store.serializers import StoreSerializer, SubcategorySerializer, ProductSerializer,RestaurantSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


# store
class StoreDetailView(generics.RetrieveAPIView):
    serializer_class = StoreSerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class StoreListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(category_type='Store')
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'category_type']  
    search_fields = ['name']  
    ordering_fields = ['name', 'created_at']  



    # restaurant
class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['name', 'rating']


class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# category
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.filter(category_type='Store')
    serializer_class = StoreSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# subcategory
class SubcategoryListListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['name', 'parent_category']
    search_fields = ['name']

class SubcategoryDetailView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# product
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['price', 'category', 'available']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'created_at']
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]