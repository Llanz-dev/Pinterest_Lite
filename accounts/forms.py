from .widgets import CustomClearableFileInput
from django.forms import ModelForm
from django import forms
from .models import UserProfile

class ProfileForm(ModelForm):
    profile_picture = forms.ImageField(widget=CustomClearableFileInput, required=False)
    
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'email', 'age', 'firstname', 'lastname', 'about', 'pronouns', 'website', 'username']
        
        