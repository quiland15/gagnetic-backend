import requests

def fetch_cj_products(page_num=1, keyword=""):
    url = f"https://api.cjdropshipping.com/api/product/search"
    payload = {
        "pageNum": page_num,
        "keyword": keyword,
        "pageSize": 10,
        "sort": "new",
    }

    headers = {
        "CJ-Access-Token": "6d0704928897419eba07bf66316aee3e",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if data.get("code") == 200:
        return data.get("data", {}).get("list", [])
    else:
        return []
