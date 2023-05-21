from .views import Profile, EditProfile, specific_board, DeleteBoard, all_pins, profile, pin_detail_user
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('<slug:board_slug>/', specific_board, name='specific-board'),
    path('pin/<str:pin_id>/', pin_detail_user, name='pin-detail-user'),    
    path('profile/pins/', all_pins, name='all-pins'),
    path('delete-board/<slug:board_slug>/<int:id>/', DeleteBoard.as_view(), name='delete-board'),
]
