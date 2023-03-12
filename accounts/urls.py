from django.urls import path
from .views import Profile, edit_profile

app_name = 'accounts'
urlpatterns = [
    path('', Profile.as_view(), name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
]