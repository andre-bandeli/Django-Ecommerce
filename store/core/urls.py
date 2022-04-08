from django.urls import path
from .views import contact, about

app_name = "core"

urlpatterns = [

    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),

]