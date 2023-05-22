from django.template.defaultfilters import slugify
from accounts.models import UserProfile
from django.utils import timezone
from django.db import models
import secrets

def generate_pin_id():
    pin_id = ''.join(map(str, [secrets.randbelow(10) for i in range(18)]))
    return pin_id

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
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)    
    user_pin = models.ManyToManyField(UserProfile, related_name='user_pin_chosen', blank=True)  
    pin_id = models.CharField(max_length=18, unique=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    destination_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='pins', blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pin_id = generate_pin_id()
        super().save(*args, **kwargs)    

class SavePinUser(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)    
    pin_id = models.CharField(max_length=18, unique=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    destination_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' - ' + self.user.email
    def save(self, *args, **kwargs):
        if not self.pk:
            self.pin_id = generate_pin_id()
        super().save(*args, **kwargs) 

class Comment(models.Model):
    text = models.CharField(max_length=50)
    hearts = models.ManyToManyField(UserProfile, related_name='comment_posts')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.text[:30]
    