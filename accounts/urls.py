from django.urls import path
from .views import Profile, EditProfile

app_name = 'accounts'
urlpatterns = [
    path('', Profile.as_view(), name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
]