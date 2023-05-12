from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm, SearchForm
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import View
from social_sharing.models import Pin
import secrets

# Create your views here.
def landing_page(request):
    pins_1 = Pin.objects.all()[:7]
    pins_2 = Pin.objects.all()[7:14]
    pins_3 = Pin.objects.all()[14:21]
    pins_4 = Pin.objects.all()[21:28]
    pins_5 = Pin.objects.all()[28:35]
    pins_6 = Pin.objects.all()[35:42]
    pins_7 = Pin.objects.all()[42:49]
    pins = Pin.objects.all().order_by('-id')
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
        

    context = {'pins': pins, 'pins_1': pins_1, 'pins_2': pins_2, 'pins_1': pins_1, 'pins_3': pins_3, 'pins_4': pins_4, 'pins_5': pins_5, 'pins_5': pins_5, 'pins_6': pins_6, 'pins_7': pins_7, 'sign_form': sign_form, 'search_form': search_form}
    return render(request, 'home/landing_page.html', context)    

class Logout(LogoutView):
    next_page = reverse_lazy('home:home')    
