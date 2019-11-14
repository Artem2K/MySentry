from unittest import TestCase

from django.test import Client

from .models import AppModel, ErrorModel
from users.models import CustomUser


TOKEN = '12345'
ERROR_LOG = {
        'error_type' : 'AssertionError',
        'error_message' : 'Message_of_error',
        'error_stack_trace' : 'stack_trace_of_error',
}
URL = f'http://127.0.0.1:8000/apps/1/error_log/'


class AppModelTest(TestCase):

    def setUp(self):
        test_user = CustomUser.objects.create(id=1, username='test_user', email="test@test.ru", password='123')
        app = AppModel.objects.create(name='test_app', token=TOKEN, user=test_user)

    def test_post_record_new_error(self):
        client = Client()
        response = client.post(URL, data=ERROR_LOG, **{'HTTP_TOKEN': TOKEN})
        self.assertEqual(response.status_code, 200)
        error_log = ErrorModel.objects.first()
        self.assertEqual(error_log.type, ERROR_LOG['error_type'])
        self.assertEqual(error_log.message, ERROR_LOG['error_message'])
        self.assertEqual(error_log.stack_trace, ERROR_LOG['error_stack_trace'])
