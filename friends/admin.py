from django.contrib import admin

from .models import FriendRequest

class FriendsAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'from_user', 'timestamp')
admin.site.register(FriendRequest, FriendsAdmin)