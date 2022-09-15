from django.contrib import admin

from user_profile.models import Friend, UserProfile, Comment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Friend)
