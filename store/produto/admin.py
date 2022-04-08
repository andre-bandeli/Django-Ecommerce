from django.contrib import admin

from .models import Category, Product, ProductHome


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "price",
        "is_available",
    ]
    list_filter = ["is_available"]
    list_editable = ["price", "is_available"]

@admin.register(ProductHome)
class ProductHomeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
    ]