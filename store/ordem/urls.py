from django.urls import path

from .views import OrderCreateView, pedidos

app_name = "ordem"

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="create"),
    path("pedidos/", pedidos, name="pedidos"),
]