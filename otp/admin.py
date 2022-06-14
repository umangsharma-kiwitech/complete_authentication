from django.contrib import admin
from .models import UserDetails


# Register your models here.
@admin.register(UserDetails)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password')
