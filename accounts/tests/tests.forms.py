from django.test import TestCase
from userprofile.forms import CustomUserCreationForm  # Update based on your folder name

class CustomUserCreationFormTest(TestCase):
    def test_valid_form(self): #if a valid form passes correctly
        form_data = { #Prepare some valid data to fill the form (non-empty fields, strong password).
            'email': 'testuser@example.com',
            'full_name': 'Test User',
            'password': 'strongpassword123'
        }
        form = CustomUserCreationForm(data=form_data) #Create a form object using the data we prepared.
        self.assertTrue(form.is_valid())#Check that the form is valid (i.e., passes all field validations),Test will fail if the form is invalid
    
    def test_invalid_form(self): #to check if an invalid form is rejected properly.
        form_data = { #Prepare invalid data: all fields are empty.
            'email': '',
            'full_name': '',
            'password': ''
        }
        form = CustomUserCreationForm(data=form_data) #Create a form object with empty/invalid data.
        self.assertFalse(form.is_valid()) #Check that the form is not valid,If somehow it becomes valid, the test will fail.
