from .views import Profile, EditProfile, SpecificBoard, DeleteBoard, all_pins
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', Profile.as_view(), name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('<slug:board_slug>/', SpecificBoard.as_view(), name='specific-board'),
    path('profile/pins/', all_pins, name='all-pins'),
    path('delete-board/<slug:board_slug>/<int:id>/', DeleteBoard.as_view(), name='delete-board'),
]
