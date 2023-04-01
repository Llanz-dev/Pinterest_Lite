from .models import Pin, Board
from django import forms

class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': False})
        }
        
    def __init__(self, *args, **kwargs):
        super(PinForm, self).__init__(*args, **kwargs)
        self.fields['board'].empty_label = None
        self.fields['board'].initial = Board.objects.first()        
        
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'is_secret']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Like "Places to Go" or "Recipes to Make"'}),
        }
        