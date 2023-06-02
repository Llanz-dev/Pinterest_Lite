from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.models import Board, Pin, OwnPin, Comment
from accounts.views import OwnPin, Board, UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm, SearchForm
from django.views.generic import ListView
from social_sharing.models import Pin
from django.urls import reverse_lazy
from django.db.models import Max
from django.views import View

import secrets

# Create your views here.
def landing_page(request):
    distinct_pins = Pin.objects.values('title').annotate(max_id=Max('id')).order_by('-max_id')
    pins = Pin.objects.filter(id__in=distinct_pins.values('max_id'), board__is_secret=False).order_by('-id')
    sign_form = SignUpForm()
    search_form = SearchForm()    

    if request.POST.get('submit') == 'log_in':         
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate the user 
        user = authenticate(request, username=email, password=password)

        # Check if authentication was successful
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:        
            error_authentication = 'Invalid email or password'
            return render(request, 'home/landing_page.html', {'error_authentication': error_authentication})                                  
    # Register
    elif request.POST.get('submit') == 'sign_up':
        sign_form = SignUpForm(request.POST)          
        if sign_form.is_valid():
            sign_form.save()
            return redirect('home:home') 
        
    context = {'pins': pins, 'sign_form': sign_form, 'search_form': search_form}
    return render(request, 'home/landing_page.html', context)    

def public_profile(request, username):
    search_form = SearchForm()
    user_profile = get_object_or_404(UserProfile, username=username)
    user_boards = Board.objects.filter(user=user_profile) 
    boards_length = len(user_boards)  
    board_pins = []    
      
    for board in user_boards:
        pin = OwnPin.objects.filter(user=user_profile, board=board)
        pin_count = pin.count()        
        board_pins.append((board, pin_count))   
    
    context = {'user_profile': user_profile, 'user_boards': user_boards, 'board_pins': board_pins, 'boards_length': boards_length, 'search_form': search_form}
    return render(request, 'accounts/public-profile.html', context)

def public_specific_board(request, username, board_slug):
    search_form = SearchForm()
    user_profile = UserProfile.objects.get(username=username)
    print('User:', user_profile)      
    print(user_profile)
    print('board:', board_slug)
    pins = OwnPin.objects.filter(board__slug=board_slug, board__user=user_profile)   
    pins_length = len(pins)
    board = Board.objects.get(slug=board_slug, user=user_profile)      
    
    context = {'board': board, 'pins': pins, 'pins_length': pins_length, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context) 

class Logout(LogoutView):
    next_page = reverse_lazy('home:home')    