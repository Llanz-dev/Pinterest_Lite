from social_sharing.models import Board, Pin, SavePinUser, Comment
from django.views.generic import RedirectView, ListView, FormView
from social_sharing.forms import PinForm, BoardForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from social_sharing.forms import BoardForm
from django.urls import reverse_lazy
from django.contrib import messages
from home.forms import SearchForm
from .models import UserProfile
from .forms import ProfileForm

class Profile(LoginRequiredMixin, CreateView):
    template_name = 'accounts/profile.html'
    model = Board
    form_class = BoardForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        board_str1 = 'Like "Places to Go" or "Recipes to Make"'
        board_str2 = 'Recipes to Make'
        user_boards = Board.objects.filter(user=self.request.user)        
        boards_length = len(user_boards)  
        board_pins = []      
        pins_length = []
        for board in user_boards:
            pin = Pin.objects.filter(board=board)
            pin_count = pin.count()        
            board_pins.append((board, pin_count))   
        for data in user_boards:
            pin = data.pin_set.all()
            pins_length.append(pin.count())    
        pins = Pin.objects.filter(board__user=self.request.user).order_by('?')
        pins_length = sum(pins_length)
        context.update({
            'pins': pins,
            'board_form': self.form_class(),
            'board_str1': board_str1,
            'board_str2': board_str2,
            'user_boards': user_boards,
            'boards_length': boards_length,
            'pins_length': pins_length,
            'board_pins': board_pins,
            'search_form': search_form        
        })
        
        return context

    def form_valid(self, form):
        board = form.save(commit=False)
        board.user = UserProfile.objects.get(email=self.request.user.email)
        board.save()
        return redirect('accounts:specific-board', board.slug)    

def profile(request):
    search_form = SearchForm()
    board_str1 = 'Like "Places to Go" or "Recipes to Make"'
    board_str2 = 'Recipes to Make'
    user_boards = Board.objects.filter(user=request.user)        
    boards_length = len(user_boards)  
    board_pins = []      
    pins_length = []
    for board in user_boards:
        pin = SavePinUser.objects.filter(board=board)
        pin_count = pin.count()        
        board_pins.append((board, pin_count))   
    for data in user_boards:
        pin = data.savepinuser_set.all()
        pins_length.append(pin.count())    
    pins = SavePinUser.objects.filter(board__user=request.user).order_by('?')
    pins_length = sum(pins_length)
    print(pins_length)    
    
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
    
class SpecificBoard(LoginRequiredMixin, ListView):
    model = Pin
    template_name = 'accounts/specific-board.html'
    context_object_name = 'pins'

    def get_queryset(self, *args, **kwargs):
        return Pin.objects.filter(board__slug=self.kwargs.get('board_slug'), board__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        board_slug = self.kwargs.get('board_slug')        
        context['board'] = get_object_or_404(Board, slug=board_slug, user=self.request.user)
        context['search_form'] = SearchForm()
        pins = self.get_queryset()
        context['pins_length'] = len(pins)
        return context

def specific_board(request, board_slug):
    search_form = SearchForm()
    pins = SavePinUser.objects.filter(board__slug=board_slug, board__user=request.user)
    board = get_object_or_404(Board, slug=board_slug, user=request.user)
    pins_length = len(pins)
    print(pins)

    context = {'board': board, 'pins': pins, 'pins_length': pins_length, 'search_form': search_form}
    return render(request, 'accounts/specific-board.html', context)    

@login_required
def pin_detail_user(request, pin_id):
    search_form = SearchForm()    
    pin = get_object_or_404(SavePinUser, pin_id=pin_id)
    pin_form = PinForm(request.user, instance=pin)
    comments = Comment.objects.filter(pin__title=pin.title)
    comment_form = CommentForm(instance=pin)
    comments_length = len(comments)

    if request.method == 'POST':
        # For save pin.
        if 'save_pin' in request.POST:
            print('save pinsss')
            pin_form = PinForm(request.user, request.POST, request.FILES)  
            if pin_form.is_valid():
                pin.user_pin.add(request.user)
                pin.save()
                print('valid:', pin.board.user)        
                instance = pin_form.save(commit=False)  
                instance.user = pin.board.user
                print('instance:', instance.user)                                
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
                return redirect('social_sharing:pin-detail', pin_id)        
                                                                                
    context = {'pin': pin, 'pin_form': pin_form, 'comments': comments, 'comments_length': comments_length, 'comment_form': comment_form,  'search_form': search_form}
    return render(request, 'social_sharing/pin-detail.html', context)

def all_pins(request):    
    search_form = SearchForm()
    pins = SavePinUser.objects.filter(board__user=request.user)
    
    context = {'pins': pins, 'search_form': search_form}
    return render(request, 'accounts/all-pins.html', context)
    
class DeleteBoard(RedirectView):
    pattern_name = 'accounts:profile'

    def get_redirect_url(self, board_slug, id, *args, **kwargs):
        get_object_or_404(Board, slug=board_slug, id=id).delete()
        return super().get_redirect_url(*args, **kwargs)