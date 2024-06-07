from django.urls import path
from .views import ProductsView, ProductsDetailView, add_remove_products_cart

app_name = "product"

urlpatterns= [
    path("products/", ProductsView.as_view(), name="products" ),
    path('products-detail/<int:pk>/', ProductsDetailView.as_view(), name="products_detail"),
    path('products/cart/<int:pk>/', add_remove_products_cart, name="products_cart")
]