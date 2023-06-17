from api import get_posts, new_post, delete_post
from settings import create_data


class TestQACloudCampApi:

    def test_get_posts(self):
        response_data = get_posts()
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

    def test_new_post(self):
        response_data = new_post(create_data)

        assert response_data['status'] == 201

        assert 'title' in response_data['result']
        assert create_data['title'] == response_data['result']['title']

        assert 'body' in response_data['result']
        assert create_data['body'] == response_data['result']['body']

        assert 'userId' in response_data['result']
        assert create_data['userId'] == response_data['result']['userId']

    def test_delete_post(self):
        response_data = new_post(create_data)
        res_id = response_data['result']['id']
        response_data_del = delete_post(res_id)

        assert response_data_del['status'] == 200
