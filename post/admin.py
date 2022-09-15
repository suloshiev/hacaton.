from django.contrib import admin
from post.models import Contact, Post, Like, Favorite


class PostAdmin(admin.ModelAdmin):

    def count_like(self, obj):
        return obj.likes.filter(like=True).count()

class FavoritAdmin(admin.ModelAdmin):
    list_display = ['owner', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Favorite, FavoritAdmin)
admin.site.register(Contact)