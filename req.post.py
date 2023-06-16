import requests
import json
from config import base_url, statuses, headers, id


pet_post_api = '/pet'
url = base_url + pet_post_api

post_data = {
    'id': id,
    'category': {
        'id': 1,
        'name': 'cats'
    },
    'name': 'kitten',
    'photoUrls': [],
    'tags': [
        {
            'id': 1,
            'name': 'черная',
        },
        {
            'id': 1,
            'name': 'пушистая',
        }
    ],
    'status': statuses[0],
}

res = requests.post(url, headers=headers, data=json.dumps(post_data))
print(res.json())
print(res.status_code)