from django.urls import path
from .views import profile, edit_profile, specific_board

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('<str:board_name>/', specific_board, name='specific-board'),
]