from django.test import TestCase
from django.urls import reverse #helps you get a url from name

class URLTests(TestCase):
    def test_signup_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
