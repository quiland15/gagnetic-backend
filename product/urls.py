from django.urls import path
from .views import ProductListAPIView
from .views import cj_product_list_view
from .views import my_products_view

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('cj-products/', cj_product_list_view, name='cj_product_list'),
    path('my-products/', my_products_view, name='my_product_list'),
]
