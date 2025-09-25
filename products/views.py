from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter

"""
ViewSets provide CRUD operations automatically when used with routers.

Performance considerations:
- Use select_related('category') to avoid N+1 queries when listing products.
- Pagination prevents huge responses for large datasets.
"""

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    """
    endpoints:
    GET     /api/products/            -> list (paginated)
    POST    /api/products/            -> create
    GET     /api/products/{pk}/       -> retrieve
    PUT     /api/products/{pk}/       -> update
    PATCH   /api/products/{pk}/       -> partial_update
    DELETE  /api/products/{pk}/       -> destroy
    """
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # change to IsAuthenticated for write ops if desired
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,]
    search_fields = ["name", "description", "sku"]
    ordering_fields = ["price", "created_at", "name"]
    ordering = ["-created_at"]
    filterset_class = ProductFilter

    def get_queryset(self):
        # Only return active products by default
        qs = super().get_queryset().filter(is_active=True)
        return qs


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
