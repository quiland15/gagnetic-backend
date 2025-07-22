import requests
import time

def fetch_my_products(page_num=1):
    time.sleep(1)  # Hindari QPS limit

    url = "https://developers.cjdropshipping.com/api2.0/v1/product/storehouse/productList"

    params = {
        "pageNum": page_num,
        "pageSize": 10,
        "language": "en"
    }

    headers = {
        "CJ-Access-Token": "API@CJ4528776@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNjAxNCIsInR5cGUiOiJBQ0NFU1NfVE9LRU4iLCJzdWIiOiJicUxvYnFRMGxtTm55UXB4UFdMWnlyVEpvYzFGeW9SeE0yVmg4T2lEZmZvZ2RSTTZIZGVUd25tdTZJc1Y5WnF6NU5YRUszWjA4KzFWanBoSGI5cUNuenlNTHJLWG80UVI5M2Y2cFNGcjJvbUEwbGsxc1Q5SGpiajVhRlZhR1psRUczdjltZjBKYzcxd3V6cDMzTmxpYjE5RlpOeXlyY0FIQSs5ak9MSGllMDdHZkJxTENFSkRTWFJvT0VmSDh3TjlOSFYrRTkyMXJhd2FmQXJadVMyTUIwNmtrVllsZjlsb2xpR2M4RHlkQSs4QS8rcGZmbm4wNW0zR204bW1VZ0lQRndCNGFqQW1hdEZwWWdTUWtkN0ozK2ZvU0hDekVPTEg1dmNYd0Y1YXZJST0iLCJpYXQiOjE3NTMwNzUzNTd9.EBAiuPa5-8g6yFgKtYhIDD-1s1ehuDNcB0mLaBeQSUI",  # Token kamu
    }

    response = requests.get(url, params=params, headers=headers)

    print("MY PRODUCTS STATUS:", response.status_code)
    print("MY PRODUCTS RAW:", response.text)

    try:
        data = response.json()
    except Exception as e:
        print("Error parsing JSON:", e)
        return []

    if data.get("code") == 200:
        return data.get("data", {}).get("list", [])
    else:
        print("My Products API error:", data.get("msg"))
        return []