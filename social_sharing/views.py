from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.forms import PinForm, BoardForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin
from social_sharing.models import Pin, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from accounts.models import UserProfile
from home.forms import SearchForm
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
            board_form = BoardForm(request.POST)      
            if board_form.is_valid():
                instance = board_form.save(commit=False)
                instance.user = UserProfile.objects.get(email=request.user.email)
                instance.save()
                return redirect('accounts:profile')   
        # For creating a pin.            
        elif 'create-pin' in request.POST:
            form = PinForm(request.user, request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                board_slug = instance.board.slug
                instance.save()
                return redirect('accounts:specific-board', board_slug)   
        
    context = {'form': form, 'board_form': board_form, 'has_board_created': has_board_created, 'search_form': search_form}
    return render(request, 'social_sharing/pin-builder.html', context)

@login_required
def pin_detail(request, pin_id):
    search_form = SearchForm()    
    pin = get_object_or_404(Pin, pin_id=pin_id)
    pin_form = PinForm(request.user, instance=pin)
    comments = Comment.objects.filter(pin=pin)
    comment_form = CommentForm()
    comments_length = len(comments)

    if request.method == 'POST':
        # For save pin.
        if 'save_pin' in request.POST:
            pin_form = PinForm(request.POST, request.FILES)  
            if pin_form.is_valid():
                instance = pin_form.save(commit=False)  
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

class PinDetail(LoginRequiredMixin, FormMixin, DetailView):
    model = Pin
    template_name = 'social_sharing/pin-detail.html'
    context_object_name = 'pin'
    form_class = CommentForm
    
    def get_object(self, queryset=None):
        pin_id = self.kwargs.get('pin_id')
        return get_object_or_404(Pin, pin_id=pin_id)

    def get_success_url(self):
        return reverse('social_sharing:pin-detail', kwargs={'pin_id': self.kwargs['pin_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pin_form'] = PinForm(instance=self.object)
        context['comments'] = Comment.objects.filter(pin=self.object)
        context['comments_length'] = len(context['comments'])
        context['search_form'] = SearchForm()
        return context   
    #    form = self.get_form()
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = self.request.user
    #         instance.pin = self.object
    #         instance.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    
def add_comment(request, pin_id):
    print('Add comment') 
    form = CommentForm(request.POST)
    if form.is_valid():        
        print(form.cleaned_data.get('title'))
    else:
        print('error', form.errors)
    return HttpResponseRedirect(reverse('social_sharing:pin-detail', kwargs={'pin_id': pin_id}))

def heart_increment(request, pin_id, text, pk):
    comment = get_object_or_404(Comment, text=text, pin__pin_id=pin_id, pk=pk)
    comment.hearts.add(request.user)
    comment.save()
    return HttpResponseRedirect(reverse('social_sharing:pin-detail', kwargs={'pin_id': pin_id}))
    
def heart_decrement(request, pin_id, text, pk):
    comment = get_object_or_404(Comment, text=text, pin__pin_id=pin_id, pk=pk)
    comment.hearts.remove(request.user)
    comment.save()
    return HttpResponseRedirect(reverse('social_sharing:pin-detail', kwargs={'pin_id': pin_id}))

def pin_delete(request, pin_id):
    pin = get_object_or_404(Pin, pin_id=pin_id)
    pin.delete()
    return redirect('accounts:specific-board', pin.board.slug)

class SavePin(CreateView):
    model = Pin

    def get_success_url(self):
        return redirect('accounts:specific-board', self.kwargs.get('board_slug'))
