from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'confirm_password', 'address_line1', 'city', 'state', 'pincode']
        widgets = {
            'password': forms.PasswordInput(),
        }

