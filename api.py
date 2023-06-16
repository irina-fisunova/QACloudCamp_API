import json
from json import JSONDecodeError

import requests
from settings import url, headers

class QACloudCampApi:

    def get_all_posts(self):
        all_posts_res = requests.get(url)

        try:
            result = all_posts_res.json()
        except JSONDecodeError:
            result = None

        return {
            'status': all_posts_res.status_code,
            'result': result,
        }

    def post_new_post(self, create_data):

        create_new_post_res = requests.post(url, headers=headers, data=json.dumps(create_data))

        return {
            'status': create_new_post_res.status_code,
            'result': create_new_post_res.json(),
        }

    def delete_post(self, post_id):
        url_1 = f"{url}/{post_id}"
        print(url_1)

        delete_post_res = requests.delete(url_1)

        return {
            'status': delete_post_res.status_code,
        }