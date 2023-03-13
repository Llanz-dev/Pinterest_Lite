from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm, SearchForm
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
class LandingPage(View):
    def get(self, request, *args, **kwargs):
        sign_form = SignUpForm()
        search_form = SearchForm()
        
        context = {'sign_form': sign_form, 'search_form': search_form}
        return render(request, 'home/landing_page.html', context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm()
        # Log in
        if request.POST.get('submit') == 'log_in':         
            if request.method == 'POST':
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
                                  
            context = {'form': form}                
            return render(request, 'home/landing_page.html', context)
        # Register
        elif request.POST.get('submit') == 'sign_up':
            form = SignUpForm(request.POST)          
            if form.is_valid():
                form.save()
                return redirect('home:home')            
                            
        context = {'form': form}
        return render(request, 'home/landing_page.html', context)


class Logout(LogoutView):
    next_page = reverse_lazy('home:home')    