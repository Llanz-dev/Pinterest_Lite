from .views import EditProfile, specific_board, DeleteBoard, profile, profile_pin_detail, profile_pin_delete
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('pin/<str:pin_id>/', profile_pin_detail, name='profile-pin-detail'),    
    path('<slug:board_slug>/', specific_board, name='specific-board'),
    path('pin-delete/<str:pin_id>/', profile_pin_delete, name='pin-delete'),    
    path('delete-board/<slug:board_slug>/<int:id>/', DeleteBoard.as_view(), name='delete-board'),
]
