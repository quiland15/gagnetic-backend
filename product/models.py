from django.db import models

class Product(models.Model):
    cj_id = models.CharField(max_length=100, unique=True)  # ID unik dari CJ
    name_en = models.CharField(max_length=255)
    sku = models.CharField(max_length=100)
    
    big_image = models.URLField(max_length=500)
    
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    your_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    stock = models.IntegerField(default=0)  # Stok CJ
    factory_stock = models.IntegerField(default=0)  # Stok pabrik
    warehouse_name = models.CharField(max_length=100)
    
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_en} - {self.sku}"