from django.test import TestCase
from django.urls import reverse

class ViewTests(TestCase):
    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
