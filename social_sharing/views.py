from django.shortcuts import render, redirect, get_object_or_404
from social_sharing.forms import PinForm, BoardForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin
from social_sharing.models import Pin, Comment
from django.http import HttpResponseRedirect
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.pin = self.object
            instance.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def heart_increment(request, pin_id, text, pk):
    comment = get_object_or_404(Comment, text=text, pin__pin_id=pin_id, pk=pk)
    comment.hearts.add(request.user)
    comment.save()
    return HttpResponseRedirect(reverse('social_sharing:pin-detail', kwargs={'pin_id': pin_id}))
    
def heart_decrement(request, pin_id, text, pk):
    comment = get_object_or_404(Comment, text=text, pin__pin_id=pin_id, pk=pk)
    print('ZZZZZZZZZZZZZZZ')
    comment.hearts.remove(request.user)
    comment.save()
    return HttpResponseRedirect(reverse('social_sharing:pin-detail', kwargs={'pin_id': pin_id}))
    # return redirect('social_sharing:pin-detail', pin_id)