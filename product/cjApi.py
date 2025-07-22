import requests
import time

def fetch_cj_products(page_num=1, keyword=""):
    time.sleep(1)  # Antisipasi QPS limit (maks 1 request per detik)

    url = "https://developers.cjdropshipping.com/api2.0/v1/product/list"

    params = {
        "pageNum": page_num,
        "keyword": keyword,
        "pageSize": 10,
        "productType": "phone accessories"
    }

    headers = {
        "CJ-Access-Token": "API@CJ4528776@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNjAxNCIsInR5cGUiOiJBQ0NFU1NfVE9LRU4iLCJzdWIiOiJicUxvYnFRMGxtTm55UXB4UFdMWnlyVEpvYzFGeW9SeE0yVmg4T2lEZmZvZ2RSTTZIZGVUd25tdTZJc1Y5WnF6NU5YRUszWjA4KzFWanBoSGI5cUNuenlNTHJLWG80UVI5M2Y2cFNGcjJvbUEwbGsxc1Q5SGpiajVhRlZhR1psRUczdjltZjBKYzcxd3V6cDMzTmxpYjE5RlpOeXlyY0FIQSs5ak9MSGllMDdHZkJxTENFSkRTWFJvT0VmSDh3TjlOSFYrRTkyMXJhd2FmQXJadVMyTUIwNmtrVllsZjlsb2xpR2M4RHlkQSs4QS8rcGZmbm4wNW0zR204bW1VZ0lQRndCNGFqQW1hdEZwWWdTUWtkN0ozK2ZvU0hDekVPTEg1dmNYd0Y1YXZJST0iLCJpYXQiOjE3NTMwNzUzNTd9.EBAiuPa5-8g6yFgKtYhIDD-1s1ehuDNcB0mLaBeQSUI",  # isi token kamu
    }

    response = requests.get(url, params=params, headers=headers)

    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text)

    try:
        data = response.json()
        print("JSON RESPONSE:", data)
    except Exception as e:
        print("ERROR PARSING:", e)
        return []

    if data.get("code") == 200:
        return data.get("data", {}).get("list", [])
    else:
        print("CJ API returned error:", data.get("msg"))
        return []