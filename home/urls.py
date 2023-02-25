from django.urls import path
from home.views import LandingPage

app_name = 'home'
urlpatterns = [
    path('', LandingPage.as_view(), name='home')
]