from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile
from django import forms

class SignUpForm(UserCreationForm):
    age = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2', 'age']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = UserProfile
        fields = ['email', 'password1', 'password2', 'age']