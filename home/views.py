from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.models import UserProfile
from .forms import SignUpForm
from django.views import View

# Create your views here.
class LandingPage(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        
        context = {'form': form}
        return render(request, 'home/landing_page.html', context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm()
        if request.POST.get('submit') == 'log_in':         
            if request.method == 'POST':
                email = request.POST['email']
                password = request.POST['password']

                user = authenticate(request, username=email, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home:home')
                else:
                    error_message = 'Invalid email or password'
                    return render(request, 'login.html', {'error_message': error_message})
            context = {'form': form}                
            return render(request, 'home/landing_page.html', context)
        elif request.POST.get('submit') == 'sign_up':
            form = SignUpForm(request.POST)          
            if form.is_valid():
                print('Success')
                form.save()
                return redirect('home:home')
            else:
                print('Error')
                for field in form:
                    for error in field.errors:
                        print(error)
                
            print('Sign up', request.POST.get('submit'))
            
        context = {'form': form}
        return render(request, 'home/landing_page.html', context)