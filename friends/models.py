from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.shortcuts import Http404,reverse


class FriendRequest(models.Model):
    to_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='to_user')
    from_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='from_user')
    timestamp = models.DateTimeField(auto_now_add= True)

