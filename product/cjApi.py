import requests

def fetch_cj_products():
    url = "https://developers.cjdropshipping.com/api2.0/v1/product/list"
    headers = {
        "CJ-Access-Token": "84abe7c3d4b2465b9b2cf57862abce9d",  # Ganti dengan token aktif
        "Content-Type": "application/json"
    }
    payload = {
        "keyword": "",     # Kata kunci pencarian produk, misalnya: "phone case"
        "pageSize": 10,    # Jumlah produk per halaman
        "pageNum": 1       # Halaman ke-berapa
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("HTTP Request Error:", e)
        return []

    try:
        data = response.json()
        print("Full Response JSON:")
        print(data)

        if isinstance(data, dict) and 'data' in data and isinstance(data['data'], dict):
            return data['data'].get('products', [])
        else:
            print("Format JSON tidak sesuai harapan.")
            return []

    except ValueError:
        print("Response bukan JSON yang valid.")
        return []