from home.views import Logout, landing_page
from django.urls import path, include

app_name = 'home'
urlpatterns = [
    path('', landing_page, name='home'),
    path('logout/', Logout.as_view(), name='log-out')
]
