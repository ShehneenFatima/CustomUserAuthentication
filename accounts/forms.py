from django import forms
from accounts.models import CustomUser  

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  #Refrencing custom user model
        fields = ['email', 'full_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password"]) #password using the set_password() is autotmatically hashed
            user.save()
        return user
