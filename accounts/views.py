from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from home.forms import SearchForm
from .models import UserProfile
from .forms import ProfileForm

from django.views import View

def profile(request):
    search_form = SearchForm()        
    print('Image:', request.user.profile_picture.url)
        
    context = {'search_form': search_form}
    return render(request, 'accounts/profile.html',context)

def edit_profile(request):
    search_form = SearchForm()      
    profile_form = ProfileForm(instance=request.user)    

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        print(profile_form.has_changed())
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('accounts:profile')
    
    context = {'search_form': search_form, 'profile_form': profile_form}
    return render(request, 'accounts/edit-profile.html', context)