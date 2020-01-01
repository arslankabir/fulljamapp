from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
     path('RecFriendRequests/<id>',views.RecFriendRequestsView, name='RecFriendRequests'),

    path('userlist/',views.SearchView.as_view(), name='userlist'),
    path('showresult/<id>',views.PeopleProfileView,name='showresult'),
    
    path('about/<id>',views.PeopleProfileAboutView, name='about'),
    path('photos/<id>',views.PeopleProfilePhotoView, name='photos'),
    path('videos/<id>',views.PeopleProfileVideoView, name='videos'),
    # url(r'^(?P<slug>[\w-]+)/$', profile_view),
    path('send_request/<id>',views.send_friend_request,name="send_request"),
    path('cencel_request/<id>',views.cancel_friend_request,name="cencel_request"),
    url(r'^accept_request/(?P<id>[\w-]+)/$', views.accept_friend_request,name="accept_request"),
    url(r'^delete_request/(?P<id>[\w-]+)/$',views.delete_friend_request,name="delete_request"),
    url(r'^unfriend/(?P<id>[\w-]+)/$',views.unfriend_user,name="unfriend"),
    url(r'^friends_list/(?P<id>[\w-]+)/$',views.friends_list,name="friends_list"),
    url(r'^friends_list_for_people/(?P<id>[\w-]+)/$',views.friends_list_for_people,name="friends_list_for_people"),


]