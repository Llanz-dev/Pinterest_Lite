from .views import EditProfile, specific_board, DeleteBoard, personal_profile, profile_pin_detail, profile_pin_delete
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', personal_profile, name='personal-profile'),
    path('<slug:board_slug>/', specific_board, name='specific-board'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('pin/<str:pin_id>/', profile_pin_detail, name='profile-pin-detail'),    
    path('pin-delete/<str:pin_id>/', profile_pin_delete, name='pin-delete'),    
    path('delete-board/<slug:board_slug>/<int:id>/', DeleteBoard.as_view(), name='delete-board'),
]
