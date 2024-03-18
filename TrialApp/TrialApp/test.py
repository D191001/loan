# from django.test import TestCase

# # from . import models

# class SimpleTest(TestCase):
#     def test_first(self):
#         self.assertEqual('Text 1', 'Text 1')
# backend/api/tests.py
from http import HTTPStatus

# from api import models
from django.test import Client, TestCase


class TestAdminStatus(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности списка задач."""
        response = self.guest_client.get('/admin/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_task_creation(self):
    #     """Проверка создания задачи."""
    #     data = {'title': 'Test', 'description': 'Test'}
    #     response = self.guest_client.post('/api/tasks/', data=data)
    #     self.assertEqual(response.status_code, HTTPStatus.CREATED)
    #     self.assertTrue(models.Task.objects.filter(title='Test').exists())
