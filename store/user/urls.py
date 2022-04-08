from django.urls import path

from user.views import login

app_name = "user"

urlpatterns = [
    path("login/", login, name="login"),
]