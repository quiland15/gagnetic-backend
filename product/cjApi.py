import requests

def fetch_cj_products(page_num=1, keyword=""):
    url = f"https://developers.cjdropshipping.com/api2.0/v1/product/list"
    payload = {
        "pageNum": page_num,
        "keyword": keyword,
        "pageSize": 10,
        "sort": "new",
        "productType" : "phone accessories"
    }

    headers = {
        "CJ-Access-Token": "API@CJ4528776@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNjAxNCIsInR5cGUiOiJBQ0NFU1NfVE9LRU4iLCJzdWIiOiJicUxvYnFRMGxtTm55UXB4UFdMWnlyVEpvYzFGeW9SeE0yVmg4T2lEZmZvZ2RSTTZIZGVUd25tdTZJc1Y5WnF6NU5YRUszWjA4KzFWanBoSGI5cUNuenlNTHJLWG80UVI5M2Y2cFNGcjJvbUEwbGsxc1Q5SGpiajVhRlZhR1psRUczdjltZjBKYzcxd3V6cDMzTmxpYjE5RlpOeXlyY0FIQSs5ak9MSGllMDdHZkJxTENFSkRTWFJvT0VmSDh3TjlOSFYrRTkyMXJhd2FmQXJadVMyTUIwNmtrVllsZjlsb2xpR2M4RHlkQSs4QS8rcGZmbm4wNW0zR204bW1VZ0lQRndCNGFqQW1hdEZwWWdTUWtkN0ozK2ZvU0hDekVPTEg1dmNYd0Y1YXZJST0iLCJpYXQiOjE3NTMwNzUzNTd9.EBAiuPa5-8g6yFgKtYhIDD-1s1ehuDNcB0mLaBeQSUI",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if data.get("code") == 200:
        return data.get("data", {}).get("list", [])
    else:
        return []
