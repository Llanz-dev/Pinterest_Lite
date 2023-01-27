from django.shortcuts import render
from django.views import View

# Create your views here.
class LandingPage(View):
    def get(self, request):
        context = {}
        return render(request, 'home/landing_page.html', context)