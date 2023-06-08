from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.models import Board, Pin, OwnPin
from django.contrib.auth.decorators import login_required
from accounts.views import OwnPin, Board, UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm, SearchForm
from django.urls import reverse_lazy
from accounts.models import Follow
from django.db.models import Max


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
            user = sign_form.save()  # Save the user object from the form
            follow_object = Follow.objects.create(user=user)  # Associate the user with the Follow object
            follow_object.save()
            return redirect('home:home')
        
    context = {'pins': pins, 'sign_form': sign_form, 'search_form': search_form}
    return render(request, 'home/landing_page.html', context)    

@login_required
def public_profile(request, username):
    search_form = SearchForm()
    user_profile = get_object_or_404(UserProfile, username=username)
    user_boards = Board.objects.filter(user=user_profile, is_secret=False) 
    boards_length = len(user_boards)  
    board_pins = []    

    # Retrieve all user boards and pins.  
    for board in user_boards:
        pin = OwnPin.objects.filter(user=user_profile, board=board)
        pin_count = pin.count()        
        board_pins.append((board, pin_count))   

    # Retrive "Follow" user table.
    follow_user = Follow.objects.get(user=user_profile)
    following_count = follow_user.get_following_count()
    followers_count = follow_user.get_followers_count()    

    # Check if request.user is following to this account user.
    do_you_follow = follow_user.follower.filter(id=request.user.id).exists()
    
    context = {'user_profile': user_profile, 'followers_count': followers_count, 'following_count': following_count, 'do_you_follow': do_you_follow, 'user_boards': user_boards, 'board_pins': board_pins, 'boards_length': boards_length, 'search_form': search_form}
    return render(request, 'accounts/public-profile.html', context)

@login_required
def public_specific_board(request, username, board_slug):
    search_form = SearchForm()
    user_profile = UserProfile.objects.get(username=username)
    pins = OwnPin.objects.filter(board__slug=board_slug, board__user=user_profile)   
    pins_length = len(pins)
    board = Board.objects.get(slug=board_slug, user=user_profile)      
    
    context = {'board': board, 'pins': pins, 'pins_length': pins_length, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context) 

class Logout(LogoutView):
    next_page = reverse_lazy('home:home')    