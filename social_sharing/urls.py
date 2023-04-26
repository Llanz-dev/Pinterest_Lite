from django.urls import path 
from .views import pin_detail, PinBuilder, PinDetail, heart_increment, heart_decrement, pin_delete, add_comment

app_name = 'social_sharing'
urlpatterns = [
    path('pin-builder/', PinBuilder.as_view(), name='pin-builder'),
    path('pin/<str:pin_id>/', pin_detail, name='pin-detail'),
    path('heart-increment/<str:pin_id>/<str:text>/<int:pk>/', heart_increment, name='heart-increment'),
    path('heart-decrement/<str:pin_id>/<str:text>/<int:pk>/', heart_decrement, name='heart-decrement'),
    path('pin-delete/<str:pin_id>/', pin_delete, name='pin-delete'),
]