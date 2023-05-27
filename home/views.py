from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm, SearchForm
from django.views.generic import ListView
from social_sharing.models import Pin
from django.urls import reverse_lazy
from django.db.models import Max
from django.views import View

import secrets

# Create your views here.
def landing_page(request):
    distinct_pins = Pin.objects.values('title').annotate(max_id=Max('id')).order_by('-max_id')
    pins = Pin.objects.filter(id__in=distinct_pins.values('max_id')).order_by('-id')
    sign_form = SignUpForm()
    search_form = SearchForm()    

    if request.POST.get('submit') == 'log_in':         
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate the user 
        user = authenticate(request, username=email, password=password)

        # Check if authentication was successful
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:        
            error_authentication = 'Invalid email or password'
            return render(request, 'home/landing_page.html', {'error_authentication': error_authentication})                                  
    # Register
    elif request.POST.get('submit') == 'sign_up':
        sign_form = SignUpForm(request.POST)          
        if sign_form.is_valid():
            sign_form.save()
            return redirect('home:home') 
        
    context = {'pins': pins, 'sign_form': sign_form, 'search_form': search_form}
    return render(request, 'home/landing_page.html', context)    

class Logout(LogoutView):
    next_page = reverse_lazy('home:home')    
