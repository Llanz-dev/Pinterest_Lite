from .widgets import CustomClearableFileInput
from django.forms import ModelForm
from django import forms
from .models import UserProfile

class ProfileForm(ModelForm):
    profile_picture = forms.ImageField(widget=CustomClearableFileInput)
    
    class Meta:
        model = UserProfile
        exclude = ['is_active', 'is_staff']
        fields = '__all__'
        
        