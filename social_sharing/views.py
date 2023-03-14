from django.shortcuts import render
from home.forms import SearchForm

# Create your views here.
def pin_builder(request):
    search_form = SearchForm()

    context = {'search_form': search_form}
    return render(request, 'social_sharing/create-pin.html', context)