import unittest
from flask import current_app
from app import create_app
import json

class AuthorAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_author_mongodb(self):
    	resp = self.client.get('/api/v1/author/mongodb')
    	self.assertEqual(resp.status_code, 200)

    def test_author_mysql(self):
    	resp = self.client.get('/api/v1/author/mysql')
    	self.assertEqual(resp.status_code, 200)

    def test_author_redis(self):
    	resp = self.client.get('/api/v1/author/redis')
    	self.assertEqual(resp.status_code, 200)

    def test_author_mysql_put(self):
    	resp = self.client.post(
    		'/api/v1/author/mysql',
    		json={"author":"test"})
    	self.assertEqual(resp.status_code, 204)

