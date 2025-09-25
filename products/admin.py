from django.contrib import admin

from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "price", "inventory_count", "is_active", "category")
    list_filter = ("is_active", "category")
    search_fields = ("name", "sku")
    raw_id_fields = ("category",)

