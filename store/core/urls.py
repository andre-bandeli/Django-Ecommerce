from django.urls import path
from .views import api

app_name = "core"

urlpatterns = [

    path("contact/", api, name="home"),
]