from django.shortcuts import render
from home.forms import SearchForm
from .forms import PinForm, BoardForm

# Create your views here.
def pin_builder(request):
    search_form = SearchForm()
    pin_form = PinForm()

    context = {'pin_form': pin_form,'search_form': search_form}
    return render(request, 'social_sharing/create-pin.html', context)