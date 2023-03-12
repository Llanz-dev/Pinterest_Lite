from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from home.forms import SearchForm
from .forms import ProfileForm
from django.views import View

class Profile(View):
    def get(self, request, *args, **kwargs):
        search_form = SearchForm()    
        context = {'search_form': search_form}
        return render(request, 'accounts/profile.html',context)

def edit_profile(request):
    profile_form = ProfileForm(instance=request.user)    
    search_form = SearchForm()  

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    
    context = {'search_form': search_form, 'profile_form': profile_form}
    return render(request, 'accounts/edit-profile.html', context)