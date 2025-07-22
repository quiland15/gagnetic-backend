import requests
import time

def fetch_cj_products(page_num=1):
    time.sleep(1)  # Hindari QPS limit

    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/myProduct/query?pageNum={page_num}&pageSize=10&language=en"

    headers = {
        "CJ-Access-Token": "API@CJ4528776@CJ:...",  # Token kamu
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
        return data.get("data", {}).get("list", [])
    else:
        print("My Products API error:", data.get("msg"))
        return []