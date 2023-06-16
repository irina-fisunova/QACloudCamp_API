import requests
from config import base_url, statuses, headers

free_api = '/pet/findByStatus'
url = base_url + free_api

for status in statuses:
    params = {
        'status': status,
    }
    res = requests.get(url, headers=headers, params=params)
    print('--------------------')
    print(res.json())
    print(res.status_code)