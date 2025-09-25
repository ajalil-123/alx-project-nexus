from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter


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
    GET     /api/products/facets/     -> category counts
    """
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # change to IsAuthenticated for write ops if desired
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["name", "description", "sku"]
    ordering_fields = ["price", "created_at", "name"]
    ordering = ["-created_at"]
    filterset_class = ProductFilter

    def get_queryset(self):
        # Only return active products by default
        return super().get_queryset().filter(is_active=True)

    @action(detail=False, methods=["get"], url_path="facets")
    def facets(self, request):
        """
        Returns counts of products per category.
        Example: GET /api/products/facets/
        """
        category_counts = (
            self.get_queryset()
            .values("category__name", "category__slug")
            .annotate(count=Count("id"))
        )
        return Response(category_counts)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
