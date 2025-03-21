from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):

    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'
    class Meta:
        db_table = 'User'