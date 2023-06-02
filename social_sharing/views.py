from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.forms import PinForm, BoardForm, CommentForm, OwnPinForm
from django.contrib.auth.decorators import login_required
from social_sharing.models import Pin, Comment, OwnPin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
from home.forms import SearchForm
from django.http import Http404
from django.urls import reverse
from .models import Board

# Create your views here
def pin_builder(request):
    search_form = SearchForm()
    form = PinForm(request.user)    
    board_form = BoardForm()
    has_board_created = Board.objects.filter(user=request.user).exists()

    if request.method == 'POST':
        # For creating a board.
        if 'create-board' in request.POST:
            print('Create Board')
            board_form = BoardForm(request.POST)      
            if board_form.is_valid():
                instance = board_form.save(commit=False)
                instance.user = UserProfile.objects.get(email=request.user.email)
                instance.save()                
                return redirect('accounts:specific-board', instance.slug)       
        # For creating a pin.            
        elif 'create-pin' in request.POST:
            print('Create Pin')            
            form = PinForm(request.user, request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                instance.users_pin.add(request.user)
                board_slug = instance.board.slug
                create_own_pin = OwnPin.objects.create(user=request.user, pin=instance, board=instance.board)
                create_own_pin.save()
                return redirect('accounts:specific-board', board_slug)
          
    context = {'form': form, 'board_form': board_form, 'has_board_created': has_board_created, 'search_form': search_form}
    return render(request, 'social_sharing/pin-builder.html', context)

@login_required
def home_pin_detail(request, pin_id):
    search_form = SearchForm()
    board_form = BoardForm()    
    has_board_created = Board.objects.filter(user=request.user).exists()    
    pin = Pin.objects.get(pin_id=pin_id)           
    own_pin_form = OwnPinForm(request.user, instance=pin)
    comments = Comment.objects.filter(pin__title=pin.title)
    comment_form = CommentForm(instance=pin)
    comments_length = len(comments)
    if request.method == 'POST':
        # For save pin.
        if 'save-pin' in request.POST:
            own_pin_form = OwnPinForm(request.user, request.POST)
            if own_pin_form.is_valid():
                pin.users_pin.add(request.user)                
                instance = own_pin_form.save(commit=False)
                instance.user = request.user
                instance.pin = pin
                instance.save()
                return redirect('accounts:specific-board', instance.board.slug)
        # For creating a board.
        elif 'create-board' in request.POST:
            print('Create Board')
            board_form = BoardForm(request.POST)      
            if board_form.is_valid():
                instance = board_form.save(commit=False)
                instance.user = UserProfile.objects.get(email=request.user.email)
                instance.save()                
                return redirect('accounts:specific-board', instance.slug)  
        # For comment add.
        elif 'comment_add' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                instance = comment_form.save(commit=False)
                instance.user = request.user
                instance.pin = pin
                instance.save()
                return redirect('social_sharing:home-pin-detail', pin_id)
            
    context = {'pin': pin, 'own_pin_form': own_pin_form, 'board_form': board_form, 'has_board_created': has_board_created, 'comments': comments, 'comments_length': comments_length,
               'comment_form': comment_form, 'search_form': search_form}
    return render(request, 'social_sharing/home-pin-detail.html', context)
    
def add_comment(request, pin_id):
    print('Add comment') 
    form = CommentForm(request.POST)
    if form.is_valid():        
        print(form.cleaned_data.get('title'))
    else:
        print('error', form.errors)
    return HttpResponseRedirect(reverse('accounts:profile-pin-detail', kwargs={'pin_id': pin_id}))

def heart_increment(request, pin_id, text, pk):
    comment = get_object_or_404(Comment, text=text, pin__pin_id=pin_id, pk=pk)
    comment.hearts.add(request.user)
    comment.save()
    return redirect('social_sharing:home-pin-detail', pin_id)
    
def heart_decrement(request, pin_id, text, pk):
    comment = get_object_or_404(Comment, text=text, pin__pin_id=pin_id, pk=pk)
    comment.hearts.remove(request.user)
    comment.save()
    return redirect('social_sharing:home-pin-detail', pin_id)

def home_pin_delete(request, pin_id):
    pin = Pin.objects.get(pin_id=pin_id)  
    pin_owner = pin.user
    
    if pin_owner == request.user:
        pin.delete()
        return redirect('home:home')           
    else:
        print('Hello World!')
    
    return Http404('There is something wrong. Please go back to home')
    
def comment_delete(request, comment_id, pin_id):
    get_object_or_404(Comment, id=comment_id).delete()
    return redirect('social_sharing:home-pin-detail', pin_id)

class SavePin(CreateView):
    model = Pin

    def get_success_url(self):
        return redirect('accounts:specific-board', self.kwargs.get('board_slug'))
