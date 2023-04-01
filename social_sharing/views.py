from django.shortcuts import render, redirect
from .forms import PinForm, BoardForm
from home.forms import SearchForm

# Create your views here.
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