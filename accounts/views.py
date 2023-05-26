from django.views.generic import TemplateView, RedirectView, ListView, FormView
from social_sharing.forms import BoardForm, OwnPinForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.models import Board, Pin, OwnPin, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from home.forms import SearchForm
from .models import UserProfile
from .forms import ProfileForm

def profile(request):
    search_form = SearchForm()
    board_str1 = 'Like "Places to Go" or "Recipes to Make"'
    board_str2 = 'Recipes to Make'
    user_boards = Board.objects.filter(user=request.user)        
    boards_length = len(user_boards)  
    board_pins = []      
    pins_length = []
    for board in user_boards:
        pin = OwnPin.objects.filter(board=board)
        pin_count = pin.count()        
        board_pins.append((board, pin_count))   
    for data in user_boards:
        pin = data.ownpin_set.all()
        pins_length.append(pin.count())    
    pins = OwnPin.objects.filter(board__user=request.user).order_by('?')
    pins_length = sum(pins_length)
    
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
                    print('board name:', board_name)
                    return redirect('accounts:profile')
                else:
                    instance.user = UserProfile.objects.get(email=request.user.email)
                    instance.save() 
                    return redirect('accounts:specific-board', instance.slug)  
        else:
            instance.user = UserProfile.objects.get(email=request.user.email)
            instance.save() 
            return redirect('accounts:specific-board', instance.slug)   

    context = {'pins': pins, 'board_form': form, 'board_str1': board_str1, 'board_str2': board_str2, 'user_boards': user_boards, 'boards_length': boards_length, 'pins_length': pins_length, 'board_pins': board_pins, 'search_form': search_form}
    return render(request, 'accounts/profile.html', context)

class EditProfile(LoginRequiredMixin, FormView):
    template_name = 'accounts/edit-profile.html'
    form_class = ProfileForm
    search_form_class = SearchForm
    success_url = reverse_lazy('accounts:profile')

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
    
def specific_board(request, board_slug):
    search_form = SearchForm()
    pins = OwnPin.objects.filter(board__slug=board_slug, board__user=request.user)
    board = get_object_or_404(Board, slug=board_slug, user=request.user)
    pins_length = len(pins)
    for pin in pins:
        print('pin:', pin.pin.user)
    
    context = {'board': board, 'pins': pins, 'pins_length': pins_length, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context) 

@login_required
def profile_pin_detail(request, pin_id):
    search_form = SearchForm()
    from_home_page = True
    own_pin_obj = OwnPin.objects.get(id=pin_id)      
    pin = Pin.objects.get(title=own_pin_obj.title)
    own_pin_form = OwnPinForm(request.user, instance=own_pin_obj)
    comments = Comment.objects.filter(pin__title=pin.title)
    comment_form = CommentForm(instance=own_pin_obj)
    comments_length = len(comments)
    
    if request.method == 'POST':
        # For save pin.
        if 'save_pin' in request.POST:
            print('save pinsss')
            own_pin_form = OwnPinForm(request.user, request.POST, request.FILES)
            if own_pin_form.is_valid():
                own_pin_obj.users_pin.add(request.user)                
                instance = own_pin_form.save(commit=False)
                instance.user = request.user
                instance.pin = pin
                instance.image = pin.image
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
            
    context = {'pin': pin, 'own_pin_form': own_pin_form, 'from_home_page': from_home_page, 'comments': comments, 'comments_length': comments_length,
               'comment_form': comment_form, 'search_form': search_form}
    return render(request, 'accounts/profile-pin-detail.html', context)    

def all_pins(request):    
    search_form = SearchForm() 
    pins = OwnPin.objects.filter(board__user=request.user)    
    
    context = {'pins': pins, 'search_form': search_form}
    return render(request, 'accounts/all-pins.html', context)
    
class DeleteBoard(RedirectView):
    pattern_name = 'accounts:profile'

    def get_redirect_url(self, board_slug, id, *args, **kwargs):
        get_object_or_404(Board, slug=board_slug, id=id).delete()
        return super().get_redirect_url(*args, **kwargs)