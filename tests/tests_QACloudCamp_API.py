import os
from api import QACloudCampApi
from settings import create_data


class TestQACloudCampApi:
    def setup(self):
        self.posts_api = QACloudCampApi

    def test_get_all_posts(self):
        response_data = self.posts_api.get_all_posts(self)
        length = len(response_data['result'])

        assert response_data['status'] == 200
        assert length == 100
        for post in response_data['result']:
            assert 'id' in post
            assert isinstance(post['id'], int)
            assert 'title' in post
            assert isinstance(post['title'], str)
            assert 'body' in post
            assert isinstance(post['body'], str)
            assert 'userId' in post
            assert isinstance(post['userId'], int)

    def test_post_new_post(self):
        response_data = self.posts_api.post_new_post(self, create_data)

        assert response_data['status'] == 201

        assert 'title' in response_data['result']
        assert create_data['title'] == response_data['result']['title']

        assert 'body' in response_data['result']
        assert create_data['body'] == response_data['result']['body']

        assert 'userId' in response_data['result']
        assert create_data['userId'] == response_data['result']['userId']

    def test_delete_post(self):
        response_data = self.posts_api.post_new_post(self, create_data)
        print(response_data['result']['id'])
        res_id = response_data['result']['id']
        response_data_del = self.posts_api.delete_post(self, res_id)

        assert response_data_del['status'] == 200
