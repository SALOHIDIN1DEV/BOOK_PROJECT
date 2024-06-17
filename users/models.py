from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(models.Model):
    image = models.ImageField(upload_to='user_images')
    
    def __str__(self) -> str:
        return f'{self.username}'
