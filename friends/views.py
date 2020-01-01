from django.shortcuts import Http404,reverse,render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect,render_to_response
from django.contrib.auth.models import User,auth #auth will use as a login part 
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView,TemplateView,RedirectView
import subprocess
from django.conf import settings
from accounts.models import UserProfile
from olympus.models import UserPost,UserComment
from friends.models import FriendRequest
from django.db.models import Q

class SearchView(TemplateView):
	template_name = 'friends/search-result.html'
	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		si = self.request.GET.get('si')
		if si == None:
			si == "There is no result related to this"
		else:
			users = UserProfile.objects.exclude(user=self.request.user).filter(Q(first_name__icontains=si) | Q(last_name__icontains=si) | Q(username__icontains=si))
			context['result_count'] = users.count
			context['users'] = users
			#context['all_posts'] = UserPost.objects.filter(uploaded_by__in=users)
			return context

def PeopleProfileView(request,id):
	people = UserProfile.objects.filter(id=id).first()
	rec_friend_requests = FriendRequest.objects.filter(to_user=request.user.userprofile).order_by('-id')
	u = people.user
	friends = people.friends.all()

	# is this user our friend
	button_status = 'none'
	if people not in request.user.userprofile.friends.all():
		button_status = 'not_friend'

		# if we have sent him a friend request
	if len(FriendRequest.objects.filter(from_user=request.user.userprofile).filter(to_user=people)) == 1:
		button_status = 'friend_request_sent'

	post = UserPost.objects.filter(uploaded_by=people).order_by('-id')
	friends_list_p = request.user.userprofile.friends.all()
	context = {
		'people':people,'all_posts':post,

		'u': u,
		'button_status': button_status,
		'friends_list': friends,
		'friends_list_p': friends_list_p,
		'rec_friend_requests': rec_friend_requests,
	}
	return render(request,'friends/people_posts.html',context)



def PeopleProfileAboutView(request,id):
	people = get_object_or_404(UserProfile, id=id)
	rec_friend_requests = FriendRequest.objects.filter(to_user=request.user.userprofile).order_by('-id')
	post = UserPost.objects.filter(uploaded_by=people).order_by('-id')
	friends = people.friends.all()
	button_status = 'none'
	if people not in request.user.userprofile.friends.all():
		button_status = 'not_friend'
	
	context = {
		'people':people,
		'button_status': button_status,
		'friends_list': friends,
		'all_posts':post,
		'friends_list_p': request.user.userprofile.friends.all(),
		'rec_friend_requests': rec_friend_requests,
	}
	return render(request,'friends/people_about.html',context)

def PeopleProfilePhotoView(request,id):
	people = get_object_or_404(UserProfile, id=id)
	rec_friend_requests = FriendRequest.objects.filter(to_user=request.user.userprofile).order_by('-id')
	post = UserPost.objects.filter(uploaded_by=people).order_by('-id')
	friends = people.friends.all()
	button_status = 'none'
	if people not in request.user.userprofile.friends.all():
		button_status = 'not_friend'
	context = {
		'people':people,
		'button_status': button_status,
		'friends_list': friends,
		'all_posts':post,
		'friends_list_p': request.user.userprofile.friends.all(),
		'rec_friend_requests': rec_friend_requests,
	}
	return render(request,'friends/people_photo.html',context)

def PeopleProfileVideoView(request,id):
	people = get_object_or_404(UserProfile, id=id)
	rec_friend_requests = FriendRequest.objects.filter(to_user=request.user.userprofile).order_by('-id')
	post = UserPost.objects.filter(uploaded_by=people)
	friends = people.friends.all()
	button_status = 'none'
	if people not in request.user.userprofile.friends.all():
		button_status = 'not_friend'
	context = {
		'people':people,
		'button_status': button_status,
		'friends_list': friends,
		'all_posts':post,
		'friends_list_p': request.user.userprofile.friends.all(),
		'rec_friend_requests': rec_friend_requests,
	}
	return render(request,'friends/people_video.html',context)

def RecFriendRequestsView(request,id):
	people = UserProfile.objects.filter(id=id).first()
	rec_friend_requests = FriendRequest.objects.filter(to_user=people).order_by('-id')
	count_request = rec_friend_requests.count
	
	context = {
		'count_request':count_request,
		'rec_friend_requests': rec_friend_requests,
		'friends_list_p': request.user.userprofile.friends.all()
	}
	return render(request,'accounts/friend_requests.html',context)


def friends_list(request,id):
	people = UserProfile.objects.filter(id=id).first()
	rec_friend_requests = FriendRequest.objects.filter(to_user=people).order_by('-id')
	button_status = 'none'
	if people not in request.user.userprofile.friends.all():
		button_status = 'not_friend'
	context = {
		'rec_friend_requests':rec_friend_requests,
		'button_status': button_status,
		'friends_list_p': request.user.userprofile.friends.all()
	}
	return render(request,'accounts/friends_list.html',context)

def friends_list_for_people(request,id):
	people = UserProfile.objects.filter(id=id).first()
	rec_friend_requests = FriendRequest.objects.filter(to_user=request.user.userprofile).order_by('-id')
	friends = people.friends.all()
	button_status = 'none'
	if people not in request.user.userprofile.friends.all():
		button_status = 'not_friend'
	context = {
		'people':people,
		'button_status': button_status,
		'friends_list': friends,
		'friends_list_p': request.user.userprofile.friends.all(),
		'rec_friend_requests':rec_friend_requests,
	}
	return render(request,'friends/people_friends.html',context)

# class SearchResultForUserSearch(ListView):
#     model = UserProfile
#     template_name = 'search-result.html'
#     context_object_name = 'users'
#     def get_queryset(self):
#         si = self.request.GET.get('si')
#         if si == None:
#             si == ""
#         else:
#             return UserProfile.objects.exclude(user=self.request.user).filter(Q(first_name__icontains=si) | Q(last_name__icontains=si) | Q(username__icontains=si))





def send_friend_request(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, id=id)
        frequest, created = FriendRequest.objects.get_or_create(from_user=request.user.userprofile,to_user=user)
        return redirect('showresult',id=user.id)

def cancel_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(UserProfile, id=id)
		frequest = FriendRequest.objects.filter(from_user=request.user.userprofile,to_user=user).first()
		frequest.delete()
		return redirect('showresult',id=user.id)

def accept_friend_request(request, id):
	user = UserProfile.objects.filter(id=id).first()
	frequest = FriendRequest.objects.filter(from_user=user, to_user=request.user.userprofile).first()
	user1 = frequest.to_user
	user2 = frequest.from_user
	user1.friends.add(user2)
	user2.friends.add(user1)
	frequest.delete()
	# return redirect('RecFriendRequests',id=user1.id)
	return redirect('showresult',id=user2.id)

def delete_friend_request(request, id):
	from_user = get_object_or_404(UserProfile, id=id)
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user.userprofile).first()
	frequest.delete()
	return HttpResponseRedirect('/friends/RecFriendRequests/{}'.format(request.user.userprofile.id))



def unfriend_user(request, id):
	unfriend_to = UserProfile.objects.filter(id=id).first()
	unfriend_from = request.user.userprofile
	user1 = unfriend_to
	user2 = unfriend_from
	user1.friends.remove(user2)
	user2.friends.remove(user1)
	# return redirect('RecFriendRequests',id=user1.id)
	return redirect('showresult',id=user1.id)

# def profile_view(request, id):
# 	p = UserProfile.objects.filter(id=id).first()
# 	u = p.user
# 	sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
# 	rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
    
# 	friends = p.friends.all()

# 	# is this user our friend
# 	button_status = 'none'
# 	if p not in request.user.profile.friends.all():
# 		button_status = 'not_friend'

# 		# if we have sent him a friend request
# 		if len(FriendRequest.objects.filter(
# 			from_user=request.user).filter(to_user=p.user)) == 1:
# 				button_status = 'friend_request_sent'

# 	context = {
# 		'u': u,
# 		'button_status': button_status,
# 		'friends_list': friends,
# 		'sent_friend_requests': sent_friend_requests,
# 		'rec_friend_requests': rec_friend_requests,
# 		'friends_list_p': request.user.userprofile.friends.all()
# 	}

# 	return render(request, "friends/people_profile.html", context)

