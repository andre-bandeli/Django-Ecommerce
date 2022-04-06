from django.urls import path
from .views import cart_add, detail_cart

app_name = "cart"

urlpatterns = [

    path("detail/", detail_cart, name="detail"),
    path("add/<int:product_id>/", cart_add, name="add"),
]