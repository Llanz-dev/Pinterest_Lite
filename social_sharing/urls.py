from django.urls import path 
from .views import home_pin_detail, heart_increment, heart_decrement, home_pin_delete, add_comment, pin_builder, comment_delete, follow, unfollow

app_name = 'social_sharing'
urlpatterns = [
    path('pin-builder/', pin_builder, name='pin-builder'),
    path('pin/<str:pin_id>/', home_pin_detail, name='home-pin-detail'),
    path('follow/<str:username>/<str:pin_id>/', follow, name='follow'),
    path('unfollow/<str:username>/<str:pin_id>/', unfollow, name='unfollow'),
    path('heart-increment/<str:pin_id>/<str:text>/<int:pk>/', heart_increment, name='heart-increment'),
    path('heart-decrement/<str:pin_id>/<str:text>/<int:pk>/', heart_decrement, name='heart-decrement'),
    path('pin-delete/<str:pin_id>/', home_pin_delete, name='pin-delete'),
    path('comment-delete/<int:comment_id>/<str:pin_id>/', comment_delete, name='comment-delete'),
]