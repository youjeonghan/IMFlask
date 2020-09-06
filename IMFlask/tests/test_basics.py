import unittest
from flask import current_app
from app import create_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_page_404(self):
        resp = self.client.get('/wrong/url')
        self.assertEqual(resp.status_code, 404)
