from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, ProductDetailView, ProductListView, ProductUpdateView, ProductDeleteView, \
    ProductCreateView

from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name




urlpatterns = [
    path("", ProductListView.as_view(), name="home"),  # Главная страница
    path("contact/", ContactTemplateView.as_view(), name="contacts"),  # Страница контактов
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product"), # Страница продукта
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"), # Страница обновления
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),

]
