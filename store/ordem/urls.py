from django.urls import path

from .views import OrderCreateView

app_name = "ordem"

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="create"),
]