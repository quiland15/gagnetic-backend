from django.urls import path
# from .views import ProductListAPIView
# from .views import cj_product_list_view
from .views import my_products_view
from .views import sync_cj_products
from .views import my_products_api

urlpatterns = [
    # path('products/', ProductListAPIView.as_view(), name='product-list'),
    # path('cj-products/', cj_product_list_view, name='cj_product_list'),
    path('my-products/', my_products_view, name='my_product_list'),
    path('sync-cj-products/', sync_cj_products, name='sync-cj-products'),
    path('my-products-api/', my_products_api, name='my_products_api'),
]
