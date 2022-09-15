from django.contrib import admin


from account.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'id']


admin.site.register(CustomUser, CustomUserAdmin)
