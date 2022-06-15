from django.contrib import admin
from .models import UserDetails, userAddresss, userCorrespondenceAddress


# Register your models here.
@admin.register(UserDetails)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password', 'email')


# Storing user address
@admin.register(userAddresss)
class address(admin.ModelAdmin):
    list_display = ('id', 'house_number', 'landmark', 'country', 'state', 'city', 'pincode')


# Storing user correspondence address
@admin.register(userCorrespondenceAddress)
class corresAddress(admin.ModelAdmin):
    list_display = ('id', 'corres_house_number', 'corres_landmark', 'country1', 'state1', 'city1', 'pincode1')
