from django.test import TestCase #importing django's Test case
from accounts.models import CustomUser
 

class CustomUserModelTest(TestCase): #ll tests inside it will run safely with a temporary database as it inherits from Test
    def test_create_user(self):
        user = CustomUser.objects.create(email='test@example.com', full_name='Test User') #manually setting email and ful name in database
        self.assertEqual(user.email, 'test@example.com')#assert that users email is exactly ".."
        self.assertEqual(user.full_name, 'Test User')#assert that users ful name is exactly ".."
        self.assertTrue(user.is_active)#check that the is_active field is True by default.
