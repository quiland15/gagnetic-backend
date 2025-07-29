from django.core.management.base import BaseCommand
from .views import fetch_cj_products
from .models import Product

class Command(BaseCommand):
    help = 'Sync CJ products every 5 minutes'

    def handle(self, *args, **kwargs):
        page = 1
        products = fetch_cj_products(page_num=page)

        for p in products:
            Product.objects.update_or_create(
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
        self.stdout.write(self.style.SUCCESS(f"Berhasil sync {len(products)} produk."))