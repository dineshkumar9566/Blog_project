from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    contact_number = models.CharField(max_length=12)
    username = models.CharField(max_length=50,unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username','contact_number']

    def __str__(self):
        return self.username
    
User = get_user_model()

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    refresh_token = models.TextField()
    access_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token for {self.user}"
  

