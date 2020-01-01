from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.shortcuts import Http404,reverse
#This is the Post model
class UserPost(models.Model):
    post_subject = models.CharField(max_length=255,blank=True, null=True)
    uploaded_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True, null=True)
    post_write =models.TextField(max_length=255,blank=True, null=True)
    post_image = models.ImageField(upload_to='pics', null=True, blank=True)
    post_video = models.FileField(upload_to='videos',blank=True, null=True)
    post_cr_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='likes',blank =True)
    def __str__(self):
         return "%s" % self.post_write

    def get_absolute_url(self):
        return reverse('postdetails',kwargs={'pk':self.pk})

class PostLike(models.Model):
    post = models.ForeignKey(UserPost,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE) 
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return "%s" % self.liked_by

class UserComment(models.Model):
    post =  models.ForeignKey(UserPost,on_delete=models.CASCADE, null=True, blank=True)
    #post_owner =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True)
    comment_by =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True)
    comment =  models.TextField(blank=True, null=True)
    c_image =  models.ImageField(upload_to='pics', null=True, blank=True)
    cm_cr_date =  models.DateTimeField(auto_now_add=True)
    cm_likes = models.ManyToManyField(User,related_name='cm_likes',blank =True)
    def __str__(self):
         return "%s" % self.comment

    def get_absolute_url(self):
        return reverse('postdetails',kwargs={'pk':self.pk})