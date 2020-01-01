
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from . import models
urlpatterns = [
    
     path('',views.home,name='index'),
     #path('showprofile/',views.showprofile,name='showprofile'),
     path('postcreate/',views.PostCreate.as_view(success_url='/postlist/')),
     path('postupdate/<int:pk>/',views.PostUpdate.as_view(success_url='/postlist/')),
     path('postdelete/<int:pk>/',views.PostDelete.as_view(success_url='/postlist/')),

     path('commentcreate/<int:pk>/',views.CommentCreate.as_view()),
     path('commentupdate/<int:pk>/',views.UpdateCommentView.as_view()),
     path('commentdelete/<int:pk>/',views.CommentDelete),
    


     path('postlist/',views.MultipleModelViewForProfilePosts.as_view()),
     path('newsfeeds/',views.MultipleModelViewForFeeds.as_view()),
     path('postdetails/<int:pk>/',views.MultipleModelViewForPostdetails.as_view(), name='postdetails'),
     path('photos/',views.MultipleModelViewForProfilePhotos.as_view()),
     path('videos/',views.MultipleModelViewForProfilevideos.as_view()),
     
     path('likepost/<int:pk>/',views.like_post,name='likepost'),
     path('likepostinpro/<int:pk>/',views.like_postinpro,name='likepostindvinpro'),
     path('likepostinpeoplepro/<int:id>/',views.like_postinPeoplePro,name='likepostinpeoplepro'),
     
     path('likepostindv/<int:pk>/',views.like_postindv,name='likepostindv'),
     path('likecomment/<int:pk>/',views.like_comment,name='likecomment'),


     path('successurl/',views.get_success_url,name='successurl'),
    

     url(r'^api/like/(?P<pk>\d+)/$', views.PostLikeAPIToggle.as_view(), name='like-api-toggle'),
     # path('like/<int:pk>/',views.PostLikeToggle.as_view()),
]