from .models import Pin
from django import forms

class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ['board']
        field = '__all__'