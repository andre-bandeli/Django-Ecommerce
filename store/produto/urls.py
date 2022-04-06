from django.urls import path
from .views import ProductDetailView, list_produtos, home

app_name = "produto"

urlpatterns = [

    path("", home.as_view(), name="home"),
    path("shop/", list_produtos.as_view(), name="shop"),
    path("produto/<slug:slug>", ProductDetailView.as_view(), name="detail"),
]