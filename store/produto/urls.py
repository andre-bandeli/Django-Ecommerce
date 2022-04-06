from django.urls import path
from .views import ProductDetailView, list_produtos

app_name = "produto"

urlpatterns = [

    path("", list_produtos.as_view(), name="list"),
    path("<slug:slug>/", list_produtos.as_view(), name="detail"),
    path("categoria/<slug:slug>/", list_produtos.as_view(), name="listByCategory"),
]