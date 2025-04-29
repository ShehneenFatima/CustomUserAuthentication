from django.test import TestCase
from userprofile.forms import CustomUserCreationForm  # Update based on your folder name

class CustomUserCreationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'email': 'testuser@example.com',
            'full_name': 'Test User',
            'password': 'strongpassword123'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        form_data = {
            'email': '',
            'full_name': '',
            'password': ''
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
