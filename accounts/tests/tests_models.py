from django.test import TestCase
from accounts.models import CustomUser
 

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create(email='test@example.com', full_name='Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.full_name, 'Test User')
        self.assertTrue(user.is_active)
