from django.template.defaultfilters import slugify
from accounts.models import UserProfile
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    is_secret = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Board, self).save(*args, **kwargs)    

class Pin(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    destination_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='pins', blank=True, null=True)
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