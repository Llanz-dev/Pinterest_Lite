from home.views import Logout, landing_page, public_profile, public_specific_board
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('', landing_page, name='home'),
    path('logout/', Logout.as_view(), name='log-out'),
    path('<str:username>/', public_profile, name='public-profile'),                
    path('<str:username>/<slug:board_slug>/', public_specific_board, name='public-specific-board'),                
]
