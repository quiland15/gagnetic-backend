import requests

def fetch_cj_products():
    url = "https://developers.cjdropshipping.com/api2.0/v1/product/list"  # contoh endpoint
    headers = {
        "CJ-Access-Token": "ISI_TOKEN_CJ_KAMU",
        "Content-Type": "application/json"
    }
    payload = {
        "keyword": "",
        "pageSize": 10,
        "pageNum": 1,
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data.get('data', {}).get('products', [])  # tergantung format asli CJ
