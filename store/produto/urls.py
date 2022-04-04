from django.urls import path
from .views import detail_produto, list_produtos

app_name = "produto"

urlpatterns = [

    path("", list_produtos.as_view(), name="listar_todos"),
    path("<slug:slug>/", detail_produto.as_view(), name="detalhar_produto"),
    path("categoria/<slug:slug>/", list_produtos.as_view(), name="listar_por_categoria"),
]