from django.shortcuts import render
from home.forms import SearchForm
from .forms import ProfileForm
from django.views import View

class Profile(View):
    def get(self, request, *args, **kwargs):
        search_form = SearchForm()    
        context = {'search_form': search_form}
        return render(request, 'accounts/profile.html',context)
    
class EditProfile(View):
    def get(self, request, *args, **kwargs):
        profile_form = ProfileForm()    
        search_form = SearchForm()    
        context = {'search_form': search_form, 'profile_form': profile_form}
        return render(request, 'accounts/edit-profile.html', context)
        