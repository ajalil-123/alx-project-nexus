from django.test import TestCase

# Create your tests here.


from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from .models import Category, Product

"""
A small test to confirm listing products works.
Run with: pytest or python -m pytest
"""

@pytest.mark.django_db
def test_list_products():
    cat = Category.objects.create(name="Phones")
    Product.objects.create(sku="SKU123", name="Phone A", price=100.00, category=cat, inventory_count=10)
    client = APIClient()
    resp = client.get(reverse("product-list"))  # DefaultRouter names endpoints product-list
    assert resp.status_code == 200
    # Check pagination structure and first result name
    assert "results" in resp.data
    assert resp.data["results"][0]["name"] == "Phone A"
