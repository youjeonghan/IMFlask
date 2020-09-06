import unittest
from flask import current_app
from app import create_app
import json


class AuthAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def get_api_headers(self, jwt=False):
        result = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        if jwt:
            result['Authorization'] = 'Bearer ' + current_app.config['TEST_ACCESS_TOKEN']

        return result

    def test_siginin(self):
        resp = self.client.post(
            '/auth/signin',
            headers=self.get_api_headers(),
            json={
                "user_id":current_app.config['ADMIN_ID'], 
                "user_pw":current_app.config['ADMIN_PW']
            }
        )
        self.assertEqual(resp.status_code, 200)

    def test_signup(self):
        resp = self.client.post(
            '/auth/signup',
            headers=self.get_api_headers(),
            json={
                "user_id":current_app.config['ADMIN_ID'], 
                "user_pw":current_app.config['ADMIN_PW']
            }
        )
        json_resp = json.loads(resp.get_data(as_text=True))
        self.assertEqual(json_resp['msg'], 'already user')

    def test_admin_required(self):
        resp = self.client.get(
            '/auth/admin_test',
            headers=self.get_api_headers(jwt=True)
        )
        self.assertEqual(resp.status_code, 200)

    def test_login_required(self):
        resp = self.client.get(
            '/auth/login_test',
            headers=self.get_api_headers(jwt=True)
        )
        self.assertEqual(resp.status_code, 200)