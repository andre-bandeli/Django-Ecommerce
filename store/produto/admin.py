from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug",]


@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "slug",
        "categoria",
        "preco",
        "is_available",
    ]
    list_filter = ["is_available",]
    list_editable = ["preco", "is_available"]