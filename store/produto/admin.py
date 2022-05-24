from django.contrib import admin

from .models import Category, Product, ProductHomeList, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
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

@admin.register(ProductHomeList)
class ProductHomeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "price",
        "is_available",
    ]
    list_filter = ["is_available"]
    list_editable = ["price", "is_available"]