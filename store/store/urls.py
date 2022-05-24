from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path("produto/", include("produto.urls")),
    path("cart/", include("cart.urls")),
    path("ordem/", include("ordem.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
