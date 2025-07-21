from django.urls import path
from .views import ProductListAPIView
from .views import cj_product_list_view

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('cj-products/', cj_product_list_view, name='cj_product_list'),
]
