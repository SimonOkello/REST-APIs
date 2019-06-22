import json
import unittest
from run import app

class TestRestApis(unittest.TestCase):
    """docstring for TestRestApis"""

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {
            "title": "This is my first blog",
            "description": "How is this day"
        }
        self.da = {
            "title": "UPDATED: Is this your first blog",
            "description": "UPDATED: This day is really good"
        }
    
    def test_post_a_blog(self):
        resp = self.client.post(path = '/blog', data = json.dumps(self.data), content_type = 'application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_all_blogs(self):
        resp = self.client.get(path = '/blog', content_type = 'application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_get_a_single_blog(self):
        post = self.client.post(path = '/blog', data = json.dumps(self.data), content_type = 'application/json')
        int_id = int(post.json['blog_id'])
        path = '/blog/{}'.format(int_id)
        response = self.client.get(path, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_editing_a_blog(self):
        post = self.client.post(path = '/blog', data = json.dumps(self.data), content_type = 'application/json')
        int_id = int(post.json['blog_id'])
        path = '/blog/{}'.format(int_id)
        response = self.client.put(path, data = json.dumps(self.da), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_a_blog(self):
        post = self.client.post(path = '/blog', data = json.dumps(self.data), content_type = 'application/json')
        int_id = int(post.json['blog_id'])
        path = '/blog/{}'.format(int_id)
        response = self.client.delete(path, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    
    if __name__ == '__main__':
        unittest.main()
    
    