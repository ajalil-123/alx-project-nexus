import django_filters
from .models import Product

"""
Advanced Product filtering:
- price_min / price_max: price range filter
- category: allows filtering by one or multiple category slugs
- name: case-insensitive contains filter
- is_active: filter active/inactive products
- inventory_min / inventory_max: optional inventory range filters
"""

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    
    inventory_min = django_filters.NumberFilter(field_name="inventory_count", lookup_expr='gte')
    inventory_max = django_filters.NumberFilter(field_name="inventory_count", lookup_expr='lte')
    
    # Multi-category filtering: comma-separated slugs
    category = django_filters.CharFilter(method='filter_by_category')
    
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ["price_min", "price_max", "inventory_min", "inventory_max", "category", "is_active", "name"]

    def filter_by_category(self, queryset, name, value):
        """
        Filter by multiple categories (comma-separated slugs).
        Example: ?category=phones,laptops
        """
        slugs = [slug.strip() for slug in value.split(',')]
        return queryset.filter(category__slug__in=slugs)
