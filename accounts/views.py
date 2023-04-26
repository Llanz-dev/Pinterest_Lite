from django.views.generic import TemplateView, RedirectView, ListView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from social_sharing.models import Board, Pin
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
        return Pin.objects.filter(board__slug=self.kwargs.get('board_slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        board_slug = self.kwargs.get('board_slug')
        context['board'] = get_object_or_404(Board, slug=board_slug)
        context['search_form'] = SearchForm()
        pins = self.get_queryset()
        context['pins_length'] = len(pins)
        return context

def all_pins(request):    
    search_form = SearchForm()
    pins = Pin.objects.filter(board__user=request.user)
    
    context = {'pins': pins, 'search_form': search_form}
    return render(request, 'accounts/all-pins.html', context)
    
class DeleteBoard(RedirectView):
    pattern_name = 'accounts:profile'

    def get_redirect_url(self, board_slug, *args, **kwargs):
        get_object_or_404(Board, slug=board_slug).delete()
        return super().get_redirect_url(*args, **kwargs)
