'''
Auth API 관련 테스트 케이스
'''
import unittest
import json
from flask import current_app
from app import create_app


class AuthAPITestCase(unittest.TestCase):
    '''Auth 테스트 케이스 클래스'''
    def setUp(self):
        '''전처리 메소드'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        '''후처리 메소드'''
        self.app_context.pop()

    @staticmethod
    def get_api_headers(jwt=False):
        '''API Header 생성 메소드'''
        result = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        if jwt:
            result['Authorization'] = 'Bearer ' + current_app.config['TEST_ACCESS_TOKEN']

        return result

    def test_signin(self):
        '''로그인 API 테스트'''
        resp = self.client.get(
            '/auth/signin',
            headers=self.get_api_headers(),
            json={
                "user_id":current_app.config['ADMIN_ID'],
                "user_pw":current_app.config['ADMIN_PW']
            }
        )
        self.assertEqual(resp.status_code, 200)

    def test_siginin_400(self):
        '''로그인 API 인자 검증 테스트'''
        resp = self.client.get(
            '/auth/signin',
            headers=self.get_api_headers(),
            json={
                "user_id":current_app.config['ADMIN_ID'],
                "user_pw":1
            }
        )
        self.assertEqual(resp.status_code, 400)

    def test_signup(self):
        '''회원가입 API 테스트'''
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
        '''관리자 검증 데코레이터 테스트'''
        resp = self.client.get(
            '/auth/admin_test',
            headers=self.get_api_headers(jwt=True)
        )
        self.assertEqual(resp.status_code, 200)

    def test_login_required(self):
        '''일반 사용자 검증 데코레이터 테스트'''
        resp = self.client.get(
            '/auth/login_test',
            headers=self.get_api_headers(jwt=True)
        )
        self.assertEqual(resp.status_code, 200)

    def test_login_optional_1(self):
        '''일반 사용자 optional1 검증 데코레이터 테스트'''
        resp = self.client.get(
            '/auth/login_optional_test',
            headers=self.get_api_headers(jwt=False)
        )
        self.assertEqual(resp.status_code, 200)

    def test_login_optional_2(self):
        '''일반 사용자 optional2 검증 데코레이터 테스트'''
        resp = self.client.get(
            '/auth/login_optional_test',
            headers=self.get_api_headers(jwt=True)
        )
        self.assertEqual(resp.status_code, 200)
