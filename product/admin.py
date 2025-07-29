from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'sku', 'sell_price', 'your_price', 'stock', 'factory_stock', 'warehouse_name')
    search_fields = ('name_en', 'sku')