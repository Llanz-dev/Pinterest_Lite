from .views import profile, edit_profile, specific_board
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('<slug:board_slug>/', specific_board, name='specific-board'),
]