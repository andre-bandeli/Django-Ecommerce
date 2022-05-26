from django.contrib import admin

from ordem.models.Item import Item
from ordem.models.Order import Order



class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ["product"]
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "email", "cpf", "paid"]
    list_filter = ["paid"]
    search_fields = ["name", "email", "cpf"]
    inlines = [ItemInline]