from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.db import models

# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """ Create a new superuser profile """
        user = self.create_user(email,name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

PRONOUN_CHOICES = (
    ('ey/em', 'ey/em'),
    ('he/him', 'he/him'),
    ('ne/nem', 'ne/nem'),
    ('she/her', 'she/her'),
    ('they/them', 'they/them'),
    ('ve/ver', 've/ver'),
    ('xe/xem', 'xe/xem'),
    ('xie/xem', 'xie/xem'),
    ('ze/zer', 'ze/zer')
)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    about = models.TextField(max_length=250, blank=True, null=True)
    pronouns = models.CharField(choices=PRONOUN_CHOICES, max_length=20, blank=True, null=True, default='ey/em')
    website = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=80, null=True)
    age = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """ Return string representation of our user """
        return self.email

class Follow(models.Model):    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    follower = models.ManyToManyField(UserProfile, related_name='followers', blank=True, null=True)
    following = models.ManyToManyField(UserProfile, related_name='following', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_followers_count(self):
        return self.follower.count()

    def get_following_count(self):
        return self.following.count()    

    def __str__(self):
        return self.user.username + ' - ' + str(self.follower.count())