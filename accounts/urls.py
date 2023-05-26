from .views import EditProfile, specific_board, DeleteBoard, all_pins, profile, profile_pin_detail
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('pins/', all_pins, name='all-pins'),    
    path('pin/<str:pin_id>/', profile_pin_detail, name='profile-pin-detail'),    
    path('<slug:board_slug>/', specific_board, name='specific-board'),
    path('delete-board/<slug:board_slug>/<int:id>/', DeleteBoard.as_view(), name='delete-board'),
]
