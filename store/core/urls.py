from django.urls import path
from .views import api

app_name = "core"

urlpatterns = [

    path("api/", api.as_view(), name="home"),
]