from .models import Pin, Board, Comment, OwnPinUser
from django import forms

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'is_secret']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Like "Places to Go" or "Recipes to Make"'}),
        }
        
class OwnPinUserForm(forms.ModelForm):
    class Meta:
        model = OwnPinUser
        fields = '__all__'
        exclude = ['user', 'pin_id', 'created_at']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': False})
        }
        
    def __init__(self, user, *args, **kwargs):
        super(OwnPinUserForm, self).__init__(*args, **kwargs)
        self.fields['board'].empty_label = None
        self.fields['board'].initial = Board.objects.first()     
        self.fields['board'].queryset = Board.objects.filter(user=user)           
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']       
        