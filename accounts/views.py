from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from social_sharing.models import Board, Pin
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
    user_boards = Board.objects.filter(user=request.user)
    boards_length = len(user_boards)    
    board_pins = []
    for board in user_boards:
        pin_count = Pin.objects.filter(board=board).count()
        board_pins.append((board, pin_count))

    if request.method == 'POST' and board_form.is_valid():
        board = board_form.save(commit=False)
        board.user = UserProfile.objects.get(email=request.user.email)
        board.save()
        return redirect('accounts:specific-board', board.slug)

    context = {'search_form': search_form, 'board_form': board_form, 'board_str1': board_str1, 'board_str2': board_str2, 'user_boards': user_boards, 'boards_length': boards_length, 'board_pins': board_pins}
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

@login_required
def specific_board(request, board_slug):
    search_form = SearchForm()
    board = Board.objects.get(slug=board_slug)      
    pins = Pin.objects.filter(board__slug=board_slug)
    pins_length = len(pins)

    # For deletion of a specific board
    if request.method == 'POST':
        board.delete()
        return redirect('accounts:profile')
    
    context = {'board_slug': board_slug, 'pins': pins, 'pins_length': pins_length, 'board': board, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context)
