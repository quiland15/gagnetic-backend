from rest_framework.views import APIView
from rest_framework.response import Response
from .cj_api import fetch_cj_products

class ProductListAPIView(APIView):
    def get(self, request):
        products = fetch_cj_products()
        return Response(products)
