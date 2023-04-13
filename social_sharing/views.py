from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from social_sharing.forms import PinForm, BoardForm, CommentForm
from social_sharing.models import Pin, Comment
from home.forms import SearchForm

# Create your views here.
@login_required
def pin_builder(request):
    search_form = SearchForm()
    pin_form = PinForm()

    if request.method == 'POST':
        pin_form = PinForm(request.POST, request.FILES)        
        if pin_form.is_valid():
            pin_form.save()
            return redirect('home:home')

    context = {'pin_form': pin_form,'search_form': search_form}
    return render(request, 'social_sharing/create-pin.html', context)

@login_required
def pin_detail(request, pin_id):
    search_form = SearchForm()    
    pin = get_object_or_404(Pin, pin_id=pin_id)
    pin_form = PinForm(instance=pin)
    comments = Comment.objects.filter(pin=pin)
    comment_form = CommentForm()
    comments_length = len(comments)
    for comment in comments:
        print(comment)

    context = {'pin': pin, 'pin_form': pin_form, 'comments': comments, 'comments_length': comments_length, 'comment_form': comment_form, 'search_form': search_form}
    return render(request, 'social_sharing/pin-detail.html', context)