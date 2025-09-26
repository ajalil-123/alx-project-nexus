
import pytest
from rest_framework.test import APIClient
from products.models import Category, Product

@pytest.mark.django_db
def test_product_list_returns_success():
    client = APIClient()
    category = Category.objects.create(name="Electronics", slug="electronics")
    Product.objects.create(name="Laptop", category=category, price=1000, sku="SKU123")

    response = client.get("/api/products/")
    assert response.status_code == 200
    assert "Laptop" in str(response.data)
