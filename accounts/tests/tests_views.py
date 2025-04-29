from django.test import TestCase
from django.urls import reverse

class ViewTests(TestCase):
    def test_profile_requires_login(self): # if the profile page correctly requires the user to log in.
        response = self.client.get(reverse('profile')) 
        self.assertEqual(response.status_code, 302)  #302, Should redirect to login page,This confirms that the profile page is protected and sends unauthenticated users to the login page.
