from django.urls import path
from .views import ProductsView, ProductsDetailView

app_name = "product"

urlpatterns= [
    path("products/", ProductsView.as_view(), name="products" ),
    path('products-detail/<int:pk>/', ProductsDetailView.as_view(), name="products_detail")
]