
import django_filters
from .models import Product

"""
FilterSet for Products:
- price_min and price_max allow price range filtering
- category filters by category slug
"""

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ["price_min", "price_max", "category", "is_active"]
