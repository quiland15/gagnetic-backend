from .cjApi import fetch_cj_products
from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.paginator import Paginator

def my_products_view(request):
    page = int(request.GET.get('page', 1))
    
    # Ambil semua data dari database
    product_list = Product.objects.all().order_by('-last_updated')

    # Pagination: 12 per halaman (ubah sesuai kebutuhan)
    paginator = Paginator(product_list, 12)
    products = paginator.get_page(page)

    context = {
        'products': products,
        'page': page,
    }
    return render(request, 'my_product_list.html', context)

@csrf_exempt
def sync_cj_products(request):
    if request.method == 'POST':
        page = int(request.GET.get('page', 1))
        products = fetch_cj_products(page_num=page)

        for p in products:
            # Gunakan get_or_create untuk menghindari duplikat
            obj, created = Product.objects.update_or_create(
                cj_id=p.get("vid"),
                defaults={
                    "name_en": p.get("nameEn", ""),
                    "sku": p.get("sku", ""),
                    "big_image": p.get("bigImage", ""),
                    "sell_price": float(p.get("sellPrice", "0").split('-')[0]),
                    "your_price": float(p.get("yourPrice", 0)),
                    "stock": p.get("stock", 0),
                    "factory_stock": p.get("factoryStock", 0),
                    "warehouse_name": p.get("warehouseName", "")
                }
            )
        
        return JsonResponse({"message": "Data berhasil disimpan ke database", "count": len(products)})

    return JsonResponse({"error": "Hanya menerima POST request"}, status=405)