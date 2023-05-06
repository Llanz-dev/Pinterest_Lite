from .views import Profile, EditProfile, SpecificBoard, DeleteBoard, all_pins, profile
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('<slug:board_slug>/', SpecificBoard.as_view(), name='specific-board'),
    path('profile/pins/', all_pins, name='all-pins'),
    path('delete-board/<slug:board_slug>/<int:id>/', DeleteBoard.as_view(), name='delete-board'),
]
