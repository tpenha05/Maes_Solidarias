from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from django.contrib import admin
from .models import MyCustomUser

admin.site.register(MyCustomUser)
