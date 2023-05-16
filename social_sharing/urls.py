from django.urls import path 
from .views import pin_detail, PinDetail, heart_increment, heart_decrement, pin_delete, add_comment, pin_builder, comment_delete

app_name = 'social_sharing'
urlpatterns = [
    path('pin-builder/', pin_builder, name='pin-builder'),
    path('pin/<str:pin_id>/', pin_detail, name='pin-detail'),
    path('heart-increment/<str:pin_id>/<str:text>/<int:pk>/', heart_increment, name='heart-increment'),
    path('heart-decrement/<str:pin_id>/<str:text>/<int:pk>/', heart_decrement, name='heart-decrement'),
    path('pin-delete/<str:pin_id>/', pin_delete, name='pin-delete'),
    path('comment-delete/<int:comment_id>/<str:pin_id>/', comment_delete, name='comment-delete'),
]