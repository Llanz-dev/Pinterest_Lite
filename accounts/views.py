from django.views.generic import TemplateView, RedirectView, ListView, FormView
from social_sharing.forms import BoardForm, OwnPinForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.models import Board, Pin, OwnPin, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from .models import UserProfile, Follow
from django.urls import reverse_lazy
from django.contrib import messages
from home.forms import SearchForm
from .forms import ProfileForm

@login_required
def personal_profile(request):
    search_form = SearchForm()
    board_str1 = 'Like "Places to Go" or "Recipes to Make"'
    board_str2 = 'Recipes to Make'
    user_boards = Board.objects.filter(user=request.user)        
    boards_length = len(user_boards)  
    board_pins = []    
      
    for board in user_boards:
        pin = OwnPin.objects.filter(board=board)
        pin_count = pin.count()        
        board_pins.append((board, pin_count))   
        
    pins = OwnPin.objects.filter(board__user=request.user).order_by('?')
    
    form = BoardForm(request.POST or None)
    if form.is_valid():        
        instance = form.save(commit=False)
        board_name = form.cleaned_data.get('name')
        boards = Board.objects.filter(user=request.user)   
        # To prevent board name duplication           
        if boards.exists():    
            for board in boards:
                if board.name == board_name:             
                    messages.error(request, 'Try a different name. You already have a board with this name!' )
                    return redirect('accounts:personal-profile')
                else:
                    instance.user = UserProfile.objects.get(email=request.user.email)
                    instance.save() 
                    return redirect('accounts:specific-board', instance.slug)  
        else:
            instance.user = UserProfile.objects.get(email=request.user.email)
            instance.save() 
            return redirect('accounts:specific-board', instance.slug)   
        
    # Retrive "Follow" user table.
    user_profile = UserProfile.objects.get(username=request.user.username)    
    follow_user = Follow.objects.get(user=user_profile)
    followers_count = follow_user.get_followers_count()
    following_count = follow_user.get_following_count()

    context = {'followers_count': followers_count, 'following_count': following_count, 'pins': pins, 'board_form': form, 'board_str1': board_str1, 'board_str2': board_str2, 'user_boards': user_boards, 'boards_length': boards_length, 'board_pins': board_pins, 'search_form': search_form}
    return render(request, 'accounts/profile.html', context)

class EditProfile(LoginRequiredMixin, FormView):
    template_name = 'accounts/edit-profile.html'
    form_class = ProfileForm
    search_form_class = SearchForm
    success_url = reverse_lazy('accounts:personal-profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form_class()
        return context

    def get_initial(self):
        return {'email': self.request.user.email}

    def form_valid(self, form):
        if form.has_changed():
            form.save()
            messages.success(self.request, 'Your profile was updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'There was an error in the form. Please try again.')
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs
    
@login_required
def specific_board(request, board_slug):
    search_form = SearchForm()
    pins = OwnPin.objects.filter(board__slug=board_slug, board__user=request.user)   
    pins_length = len(pins)
    board = get_object_or_404(Board, slug=board_slug, user=request.user)
    
    context = {'board': board, 'pins': pins, 'pins_length': pins_length, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context) 

@login_required
def profile_pin_detail(request, pin_id):
    search_form = SearchForm() 
    own_pin = OwnPin.objects.get(id=pin_id)  
    pin = Pin.objects.get(title=own_pin.pin.title, id=own_pin.pin.id)
    own_pin_form = OwnPinForm(request.user, instance=own_pin)
    comments = Comment.objects.filter(pin__title=pin.title)
    comment_form = CommentForm(instance=own_pin)
    comments_length = len(comments)
    
    if request.method == 'POST':
        # For save pin.
        if 'save_pin' in request.POST:
            own_pin_form = OwnPinForm(request.user, request.POST)
            if own_pin_form.is_valid():
                instance = own_pin_form.save(commit=False)
                instance.user = request.user
                instance.pin = pin
                instance.save()
                return redirect('accounts:specific-board', instance.board.slug)
        # For comment add.
        elif 'comment_add' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                instance = comment_form.save(commit=False)
                instance.user = request.user
                instance.pin = pin
                instance.save()
                return redirect('accounts:profile-pin-detail', pin_id)

    # Retrive "Follow" user table.
    user_profile = get_object_or_404(UserProfile, username=pin.user.username)    
    follow_user = Follow.objects.get(user=user_profile)
    following_count = follow_user.get_following_count()
    followers_count = follow_user.get_followers_count()
    
    # Check if request.user is following to this account user.
    do_you_follow = follow_user.follower.filter(id=request.user.id).exists()     
    
    context = {'own_pin': own_pin, 'own_pin_form': own_pin_form, 'following_count': following_count, 'followers_count': followers_count, 'do_you_follow': do_you_follow, 'comments': comments, 'comments_length': comments_length,
               'comment_form': comment_form, 'search_form': search_form}
    return render(request, 'accounts/profile-pin-detail.html', context)    

@login_required
def profile_pin_delete(request, pin_id):
    own_pin_object = OwnPin.objects.filter(user=request.user, id=pin_id)   
    pin = Pin.objects.get(title=own_pin_object.first().pin.title)      
    own_pin_object = OwnPin.objects.filter(user=request.user, pin__title=pin.title)   
    own_pin_count = len(own_pin_object)                
    pin_owner = pin.user
    own_pin = OwnPin.objects.get(user=request.user, id=pin_id)
    board_slug = own_pin.board.slug
    
    if pin_owner == request.user:
        pin.delete()
        return redirect('accounts:specific-board', board_slug)        
    
    if own_pin.user == request.user:
        own_pin_delete = get_object_or_404(OwnPin, id=pin_id)
        own_pin_delete.delete()
            
    if own_pin_count == 1:
        pin.users_pin.remove(request.user)                    
        
    return redirect('accounts:specific-board', board_slug)   

@login_required
def follow(request, username):
    # For to save the request.user to user account. Follower
    user_profile = UserProfile.objects.get(username=username)
    follow_user = Follow.objects.get(user=user_profile)
    follow_user.follower.add(request.user)
    # For to save the user account to request.user. Following
    request_user = UserProfile.objects.get(username=request.user.username)
    follow_request_user = Follow.objects.get(user=request_user)
    follow_request_user.following.add(user_profile)        
    return redirect('home:public-profile', username)

@login_required
def unfollow(request, username):
    # For to save the request.user to user account.
    user_profile = UserProfile.objects.get(username=username)
    follow_user = Follow.objects.get(user=user_profile)
    follow_user.follower.remove(request.user)
    # For to save the user account to request.user.
    request_user = UserProfile.objects.get(username=request.user.username)
    follow_request_user = Follow.objects.get(user=request_user)    
    follow_request_user.following.remove(user_profile) 
    return redirect('home:public-profile', username)  

@login_required
def profile_follow_pin(request, username, pin_id):
    # For to save the request.user to user account. Follower
    user_profile = UserProfile.objects.get(username=username)
    follow_user = Follow.objects.get(user=user_profile)
    follow_user.follower.add(request.user)
    # For to save the user account to request.user. Following
    request_user = UserProfile.objects.get(username=request.user.username)
    follow_request_user = Follow.objects.get(user=request_user)
    follow_request_user.following.add(user_profile)        
    return redirect('accounts:profile-pin-detail', pin_id)   

@login_required
def profile_unfollow_pin(request, username, pin_id):
    # For to save the request.user to user account.
    user_profile = UserProfile.objects.get(username=username)
    follow_user = Follow.objects.get(user=user_profile)
    follow_user.follower.remove(request.user)
    # For to save the user account to request.user.
    request_user = UserProfile.objects.get(username=request.user.username)
    follow_request_user = Follow.objects.get(user=request_user)    
    follow_request_user.following.remove(user_profile)       
    return redirect('accounts:profile-pin-detail', pin_id)   
    
class DeleteBoard(RedirectView):
    pattern_name = 'accounts:personal-profile'

    def get_redirect_url(self, board_slug, id, *args, **kwargs):
        get_object_or_404(Board, slug=board_slug, id=id).delete()
        return super().get_redirect_url(*args, **kwargs)