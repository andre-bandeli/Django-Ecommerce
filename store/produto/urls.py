from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import ProductListView, ProductDetailView, home

app_name = "produto"

urlpatterns = [
    path("", home, name="home"),
    path("list/", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)