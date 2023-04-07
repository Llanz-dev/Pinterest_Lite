from django.urls import path 
from .views import pin_builder, pin_detail

app_name = 'social_sharing'
urlpatterns = [
    path('pin-builder/', pin_builder, name='pin-builder'),
    path('pin/<str:pin_id>/', pin_detail, name='pin-detail'),
]