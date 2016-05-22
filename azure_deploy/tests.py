from django.test import TestCase

class AzureTest(TestCase):

    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_login_success(self):
        r = self.client.get('/login/complete/success')
        self.assertEqual(r.status_code, 200)
