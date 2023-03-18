from accounts.models import UserProfile
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=50)
    is_secret = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pin(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    destination_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='pins')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    hearts = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:30]