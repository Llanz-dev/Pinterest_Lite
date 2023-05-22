from django.contrib import admin
from .models import Board, Pin, Comment, OwnPinUser

# Register your models here.
admin.site.register(Board)
admin.site.register(Pin)
admin.site.register(Comment)
admin.site.register(OwnPinUser)
