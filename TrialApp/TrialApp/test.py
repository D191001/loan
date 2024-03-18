from http import HTTPStatus

from django.test import Client, TestCase


class TestAdminStatus(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности админки."""
        response = self.guest_client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
