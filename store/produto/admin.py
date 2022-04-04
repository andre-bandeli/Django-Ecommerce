from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "created", "modified"]


@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "slug",
        "categoria",
        "preco",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["preco", "is_available"]