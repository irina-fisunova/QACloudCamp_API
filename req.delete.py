import requests
from config import base_url, headers, id

free_api = f"/pet/{id}"
url = base_url + free_api

res = requests.delete(url, headers=headers)
print(res.json())
print(res.status_code)