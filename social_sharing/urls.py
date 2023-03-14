from django.urls import path 
from .views import pin_builder

app_name = 'social_sharing'
urlpatterns = [
    path('', pin_builder, name='pin-builder')
]