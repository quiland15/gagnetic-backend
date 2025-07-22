import requests
import time

# Ganti dengan token kamu
ACCESS_TOKEN = "API@CJ4528776@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNjAxNCIsInR5cGUiOiJBQ0NFU1NfVE9LRU4iLCJzdWIiOiJicUxvYnFRMGxtTm55UXB4UFdMWnlyVEpvYzFGeW9SeE0yVmg4T2lEZmZvZ2RSTTZIZGVUd25tdTZJc1Y5WnF6NU5YRUszWjA4KzFWanBoSGI5cUNuenlNTHJLWG80UVI5M2Y2cFNGcjJvbUEwbGsxc1Q5SGpiajVhRlZhR1psRUczdjltZjBKYzcxd3V6cDMzTmxpYjE5RlpOeXlyY0FIQSs5ak9MSGllMDdHZkJxTENFSkRTWFJvT0VmSDh3TjlOSFYrRTkyMXJhd2FmQXJadVMyTUIwNmtrVllsZjlsb2xpR2M4RHlkQSs4QS8rcGZmbm4wNW0zR204bW1VZ0lQRndCNGFqQW1hdEZwWWdTUWtkN0ozK2ZvU0hDekVPTEg1dmNYd0Y1YXZJST0iLCJpYXQiOjE3NTMwNzUzNTd9.EBAiuPa5-8g6yFgKtYhIDD-1s1ehuDNcB0mLaBeQSUI"  # <- potong untuk keamanan

# Ambil varian produk (SKU anak)
def get_variants_by_product_id(product_id):
    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/variant/query?productId={product_id}"
    headers = {
        "CJ-Access-Token": ACCESS_TOKEN
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200:
                return data.get("data", [])
    except Exception as e:
        print("Error get_variants:", e)

    return []

# Ambil stok berdasarkan SKU varian
def fetch_stock_by_sku(sku):
    time.sleep(0.5)  # Hindari limit
    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/stock/queryBySku?sku={sku}"
    headers = {
        "CJ-Access-Token": ACCESS_TOKEN
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200:
                return data.get("data", [])
            else:
                print("SKU stock error:", data.get("message"))
        else:
            print("SKU stock failed:", response.status_code)
    except Exception as e:
        print("Exception SKU:", e)

    return []

# Ambil produk dari akun kamu (My Product)
def fetch_cj_products(page_num=1):
    time.sleep(0.5)

    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/myProduct/query?pageNum={page_num}&pageSize=10&language=en"
    headers = {
        "CJ-Access-Token": ACCESS_TOKEN
    }

    response = requests.get(url, headers=headers)
    print("MY PRODUCTS STATUS:", response.status_code)

    try:
        data = response.json()
    except Exception as e:
        print("JSON Error:", e)
        return []

    if data.get("code") == 200:
        products = data.get("data", {}).get("content", [])

        for p in products:
            product_id = p.get("productId")
            variants = get_variants_by_product_id(product_id)

            total_cj_stock = 0
            total_factory_stock = 0
            warehouses = set()

            for variant in variants:
                sku = variant.get("variantSku")
                stock_info = fetch_stock_by_sku(sku)
                for s in stock_info:
                    total_cj_stock += s.get("cjSellable", 0)
                    total_factory_stock += s.get("factorySellable", 0)
                    warehouses.add(s.get("warehouseName", ""))

            p["stock"] = total_cj_stock
            p["factoryStock"] = total_factory_stock
            p["warehouseName"] = ", ".join(filter(None, warehouses))

            # Harga jual (50% keuntungan)
            try:
                price_range = p.get("sellPrice", "0-0").split('-')
                base_price = float(price_range[0])
                p["yourPrice"] = round(base_price * 1.5, 2)
            except:
                p["yourPrice"] = "N/A"

        return products
    else:
        print("My Product API Error:", data.get("msg"))
        return []