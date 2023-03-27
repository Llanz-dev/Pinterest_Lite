from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from social_sharing.forms import BoardForm
from django.contrib import messages
from home.forms import SearchForm
from .models import UserProfile
from .forms import ProfileForm

@login_required
def profile(request):
    search_form = SearchForm()
    board_str1 = 'Like "Places to Go" or "Recipes to Make"'
    board_str2 = 'Recipes to Make'
    board_form = BoardForm(request.POST or None)

    if request.method == 'POST' and board_form.is_valid():
        board = board_form.save(commit=False)
        board.user = UserProfile.objects.get(email=request.user.email)
        board.save()
        return redirect('accounts:specific-board', board.name)

    context = {'search_form': search_form, 'board_form': board_form, 'board_str1': board_str1, 'board_str2': board_str2}
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    search_form = SearchForm()      
    profile_form = ProfileForm(instance=request.user)    

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid() and profile_form.has_changed():
            profile_form.save()         
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('accounts:profile')
    
    context = {'search_form': search_form, 'profile_form': profile_form}
    return render(request, 'accounts/edit-profile.html', context)

def specific_board(request, board_name):
    search_form = SearchForm()      
    
    print('Congratulations!')
    
    print(board_name)
    context = {'board_name': board_name, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context)
