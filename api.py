import json
from json import JSONDecodeError

import requests
from settings import url, headers


def get_posts():
    all_posts_res = requests.get(url)

    try:
        result = all_posts_res.json()
    except JSONDecodeError:
        result = None

    return {
        'status': all_posts_res.status_code,
        'result': result,
    }


def new_post(create_data):
    create_new_post_res = requests.post(url, headers=headers, data=json.dumps(create_data))

    return {
        'status': create_new_post_res.status_code,
        'result': create_new_post_res.json(),
    }


def delete_post(post_id):
    delete_post_res = requests.delete(f"{url}/{post_id}")

    return {
        'status': delete_post_res.status_code,
    }
