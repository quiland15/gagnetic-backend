import requests

def fetch_cj_products(page_num=1, page_size=10):
    url = 'https://developers.cjdropshipping.com/api2.0/v1/product/list'
    headers = {
        'CJ-Access-Token': '6d0704928897419eba07bf66316aee3e',  # ganti dengan token asli
        'Content-Type': 'application/json',
    }
    body = {
        "pageNum": page_num,
        "pageSize": page_size
    }
    response = requests.post(url, json=body, headers=headers)

    if response.status_code == 200:
        return response.json().get('data', {}).get('list', [])
    else:
        return []
