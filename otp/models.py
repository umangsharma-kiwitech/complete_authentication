from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserDetails(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    password = models.CharField(max_length=160)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'username', 'password']

    def __str__(self):
        return self.email
