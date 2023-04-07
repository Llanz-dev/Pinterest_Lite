from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PinForm, BoardForm
from .models import Pin
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
    pin = get_object_or_404(Pin, pin_id=pin_id)
    return render(request, 'social_sharing/pin-detail.html', {'pin': pin})