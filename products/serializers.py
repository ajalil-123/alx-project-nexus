
from rest_framework import serializers
from .models import Product, Category

"""
Serializers convert model instances to JSON and validate incoming input.
We include a read-only nested category and a write-only category_id field
to simplify create/update requests.
"""

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class ProductSerializer(serializers.ModelSerializer):
    # Read-only nested representation of category
    category = CategorySerializer(read_only=True)
    # Accept category_id to set foreign key on write operations
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "sku",
            "name",
            "slug",
            "description",
            "price",
            "inventory_count",
            "is_active",
            "category",
            "category_id",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "slug", "created_at", "updated_at")
