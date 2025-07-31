from .cjApi import fetch_cj_products
from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.core import serializers
from django.http import JsonResponse

def my_products_api(request):
    page = int(request.GET.get('page', 1))
    product_list = Product.objects.all().order_by('-last_updated')
    paginator = Paginator(product_list, 12)
    products = paginator.get_page(page)

    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name_en': product.name_en,
            'sku': product.sku,
            'big_image': product.big_image,
            'sell_price': float(product.sell_price),
            'your_price': float(product.your_price),
            'stock': product.stock,
            'factory_stock': product.factory_stock,
            'warehouse_name': product.warehouse_name,
        })

    return JsonResponse({
        'page': page,
        'total_pages': paginator.num_pages,
        'total_items': paginator.count,
        'products': data,
    })

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

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Tambahkan job tiap 5 menit
    scheduler.add_job(
        sync_cj_products,
        trigger="interval",
        minutes=5,
        id="sync_cj_products",
        replace_existing=True,
    )

    scheduler.start()
    print("Scheduler started.")