from home.views import LandingPage, Logout
from django.urls import path, include

app_name = 'home'
urlpatterns = [
    path('', LandingPage.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='log-out')
]
