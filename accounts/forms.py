# userprofile/forms.py

from django import forms
from accounts.models import CustomUser  # Make sure you're importing CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  # Make sure to reference your custom user model here
        fields = ['email', 'full_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password"])
            user.save()
        return user
