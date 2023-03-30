from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from social_sharing.forms import BoardForm
from social_sharing.models import Board
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
    user_boards = Board.objects.filter(user=request.user)
    boards_length = len(user_boards)
    # Check if there is any data in the queryset
    if user_boards.exists():
        # If there is data, do something
        print(user_boards)
        # ...
    else:
        print('No object Llanz')
        # If there is no data, do something else
        # ...

    if request.method == 'POST' and board_form.is_valid():
        board = board_form.save(commit=False)
        board.user = UserProfile.objects.get(email=request.user.email)
        board.save()
        return redirect('accounts:specific-board', board.name)

    context = {'search_form': search_form, 'board_form': board_form, 'board_str1': board_str1, 'board_str2': board_str2, 'user_boards': user_boards, 'boards_length': boards_length}
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
    
    context = {'board_name': board_name, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context)
