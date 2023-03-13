from django.urls import path
from .views import profile, edit_profile

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
]