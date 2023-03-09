from home.forms import SearchForm
from django.shortcuts import render
from django.views import View

class Profile(View):
    def get(self, request, *args, **kwargs):
        search_form = SearchForm()    
        context = {'search_form': search_form}
        return render(request, 'accounts/profile.html',context)
        