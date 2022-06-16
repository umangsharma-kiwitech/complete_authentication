from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# table for user details

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
        return self.username


# user address table

class userAddresss(models.Model):
    useradd = models.ForeignKey(UserDetails,on_delete=models.SET,null=True)
    house_number = models.CharField(max_length=50)
    landmark = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    REQUIRED_FIELDS = ['house_number', 'landmark', 'country', 'state', 'city', 'pincode']

    def __str__(self):
        return self.house_number


# user correspondence address

class userCorrespondenceAddress(models.Model):
    corres_house_number = models.CharField(max_length=50)
    corres_landmark = models.CharField(max_length=100)
    country1 = models.CharField(max_length=50)
    state1 = models.CharField(max_length=50)
    city1 = models.CharField(max_length=100)
    pincode1 = models.IntegerField()
    REQUIRED_FIELDS1 = ['corres_house_number', 'corres_landmark', 'country', 'state', 'city', 'pincode']

    def __str__(self):
        return self.corres_house_number


