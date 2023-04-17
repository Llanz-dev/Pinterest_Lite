from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.forms import PinForm, BoardForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from social_sharing.models import Pin, Comment
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from home.forms import SearchForm

# Create your views here.
class PinBuilder(LoginRequiredMixin, CreateView):
    model = Pin
    form_class = PinForm
    template_name = 'social_sharing/pin-builder.html'
    success_url = reverse_lazy('home:home')

@login_required
def pin_detail(request, pin_id):
    search_form = SearchForm()    
    pin = get_object_or_404(Pin, pin_id=pin_id)
    pin_form = PinForm(instance=pin)
    comments = Comment.objects.filter(pin=pin)
    form = CommentForm()
    comments_length = len(comments)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.pin = pin
            instance.save()
            return HttpResponseRedirect(reverse('social_sharing:pin-detail', kwargs={'pin_id': pin_id}))
        else:
            print(form.errors)

    context = {'pin': pin, 'pin_form': pin_form, 'comments': comments, 'comments_length': comments_length, 'form': form, 'search_form': search_form}
    return render(request, 'social_sharing/pin-detail.html', context)
