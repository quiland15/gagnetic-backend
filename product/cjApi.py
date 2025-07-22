import requests
import time

# Ganti dengan token kamu
ACCESS_TOKEN = "API@CJ4528776@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNjAxNCIsInR5cGUiOiJBQ0NFU1NfVE9LRU4iLCJzdWIiOiJicUxvYnFRMGxtTm55UXB4UFdMWnlyVEpvYzFGeW9SeE0yVmg4T2lEZmZvZ2RSTTZIZGVUd25tdTZJc1Y5WnF6NU5YRUszWjA4KzFWanBoSGI5cUNuenlNTHJLWG80UVI5M2Y2cFNGcjJvbUEwbGsxc1Q5SGpiajVhRlZhR1psRUczdjltZjBKYzcxd3V6cDMzTmxpYjE5RlpOeXlyY0FIQSs5ak9MSGllMDdHZkJxTENFSkRTWFJvT0VmSDh3TjlOSFYrRTkyMXJhd2FmQXJadVMyTUIwNmtrVllsZjlsb2xpR2M4RHlkQSs4QS8rcGZmbm4wNW0zR204bW1VZ0lQRndCNGFqQW1hdEZwWWdTUWtkN0ozK2ZvU0hDekVPTEg1dmNYd0Y1YXZJST0iLCJpYXQiOjE3NTMwNzUzNTd9.EBAiuPa5-8g6yFgKtYhIDD-1s1ehuDNcB0mLaBeQSUI"  # <- potong untuk keamanan

# Ambil stok berdasarkan vid
def fetch_stock_by_vid(vid):
    time.sleep(0.1)  # Hindari limit request per detik

    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/stock/queryByVid?vid={vid}"
    headers = {
        "CJ-Access-Token": ACCESS_TOKEN
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if data.get("code") == 200:
                return data.get("data", [])
            else:
                print("Stock API error:", data.get("message"))
        except Exception as e:
            print("Error parsing stock JSON:", e)
    else:
        print("Failed stock request:", response.status_code)

    return []  # fallback

# Ambil produk dari "My Product"
def fetch_cj_products(page_num=1):
    time.sleep(0.1)  # Hindari QPS limit

    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/myProduct/query?pageNum={page_num}&pageSize=10&language=en"
    headers = {
        "CJ-Access-Token": ACCESS_TOKEN
    }

    response = requests.get(url, headers=headers)

    print("MY PRODUCTS STATUS:", response.status_code)
    print("MY PRODUCTS RAW:", response.text)

    try:
        data = response.json()
    except Exception as e:
        print("Error parsing JSON:", e)
        return []

    if data.get("code") == 200:
        products = data.get("data", {}).get("content", [])

        # Tambahkan data stok untuk setiap produk
        for p in products:
            vid = p.get("vid")
            stock_data = fetch_stock_by_vid(vid)

            if stock_data:
                # Tambahkan total stok dari semua gudang
                total_stock = sum([w.get("sellable", 0) for w in stock_data])
                p["stock"] = total_stock

                # Bisa juga tambahkan nama gudang jika mau
                p["warehouseName"] = ", ".join([w.get("warehouseName", "") for w in stock_data])
            else:
                p["stock"] = "N/A"
                p["warehouseName"] = "Unknown"

            try:
                price_range = p.get("sellPrice", "0-0").split('-')
                base_price = float(price_range[0])
                p["yourPrice"] = round(base_price * 1.5, 2)
            except:
                p["yourPrice"] = "N/A"

        return products

    else:
        print("My Products API error:", data.get("msg"))
        return []