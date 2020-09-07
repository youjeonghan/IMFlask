'''
API V1 Auth API 관련 테스트 케이스
'''
import unittest
from app import create_app


class AuthorAPITestCase(unittest.TestCase):
    '''API V1 Auth 테스트 케이스 클래스'''

    def setUp(self):
        '''전처리 메소드'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        '''후처리 메소드'''
        self.app_context.pop()

    def test_author_mongodb(self):
        '''Get Author in MongoDB API 테스트'''
        resp = self.client.get('/api/v1/author/mongodb')
        self.assertEqual(resp.status_code, 200)

    def test_author_mysql(self):
        '''Get Author in Mysql API 테스트'''
        resp = self.client.get('/api/v1/author/mysql')
        self.assertEqual(resp.status_code, 200)

    def test_author_redis(self):
        '''Get Author in Redis API 테스트'''
        resp = self.client.get('/api/v1/author/redis')
        self.assertEqual(resp.status_code, 200)

    def test_author_mysql_put(self):
        '''Insert Author in Mysql API 테스트'''
        resp = self.client.post(
            '/api/v1/author/mysql',
            json={"author":"test"})
        self.assertEqual(resp.status_code, 204)
