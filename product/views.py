from rest_framework.views import APIView
from rest_framework.response import Response
from .cjApi import fetch_cj_products
from django.shortcuts import render

class ProductListAPIView(APIView):
    def get(self, request):
        products = fetch_cj_products()
        return Response(products)

def cj_product_list_view(request):
    keyword = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))

    products = fetch_cj_products(page_num=page, keyword=keyword)
    
    context = {
        'products': products,
        'keyword': keyword,
        'page': page,
    }
    return render(request, 'cj_product_list.html', context)

def my_products_view(request):
    page = int(request.GET.get('page', 1))
    products = fetch_my_products(page_num=page)

    context = {
        'products': products,
        'page': page
    }
    return render(request, 'my_product_list.html', context)