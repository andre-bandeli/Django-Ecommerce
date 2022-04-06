from django.urls import path
from .views import index

app_name = "cart"

urlpatterns = [

    path("detail/", index, name="detail"),
]