from django.urls import path 
from .views import pin_detail, PinBuilder

app_name = 'social_sharing'
urlpatterns = [
    path('pin-builder/', PinBuilder.as_view(), name='pin-builder'),
    path('pin/<str:pin_id>/', pin_detail, name='pin-detail'),
]