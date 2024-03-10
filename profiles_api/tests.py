from django.test import TestCase, Client
from rest_framework import status

client = Client()


class ProfileTestCase(TestCase):
    def setUp(self):
        self.url = '/api/profile/'

    # 함수명 앞에 test_가 있어야 테스트가 실행된다.
    def test_프로필_가져오기(self):
        response = client.get(self.url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


