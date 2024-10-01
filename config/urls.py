from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),  # Подключение к URL'ам приложения catalog
    path("blog/", include("blog.urls", namespace="blog")),  # Подключение к URL'ам приложения blog
    path("users/", include("users.urls", namespace="users")),  # Подключение к URL'ам приложения users
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
