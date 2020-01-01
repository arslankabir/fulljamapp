from django.shortcuts import Http404,reverse,render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect,render_to_response
from django.contrib.auth.models import User,auth #auth will use as a login part 
from django.contrib import messages
from .models import UserPost,UserComment,PostLike,UserProfile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView,TemplateView,RedirectView
import subprocess
from django.conf import settings
from friends.models import FriendRequest
from django.db.models import Q
# Create your views here.
# @method_decorator(login_required, name='dispatch')






def showprofile(request):
    return render(request,'posts.html')

def home(request):
    return redirect('/accounts/register/')

# @method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = UserPost
    fields = ['post_subject','post_write','post_image','post_video']
    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.userprofile
        self.object.save()
        return redirect('/postlist/')


class PostUpdate(UpdateView):
    model = UserPost
    template_name='olympus/userpost_update_form.html'
    fields = ['post_subject','post_write','post_image','post_video']

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(PostUpdate, self).get_object()
        if not obj.uploaded_by == self.request.user.userprofile:
            raise Http404
        return obj  

class PostDelete(DeleteView):
    model = UserPost
    #used this method to not confirm just delete (not post just delete and get)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    #template_name='olympus/userpost_form.html'
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(PostDelete, self).get_object()
        if not obj.uploaded_by == self.request.user.userprofile:
            raise Http404
        return obj  

# class PostList(ListView):
#     model = UserPost
#     context_object_name = 'all_posts'
#     template_name='olympus/userpost_form.html'
#     def get_queryset(self):
#         return UserPost.objects.filter(uploaded_by=self.request.user.userprofile).order_by('-id')

class CommentCreate(CreateView):
    model = UserComment
    # template_name='olympus/newsfeeds.html'
    fields = ['comment','c_image']
    def form_valid(self, form):
        mypost = get_object_or_404(UserPost, pk=self.kwargs['pk'])
        self.object = form.save()
        self.object.comment_by = self.request.user.userprofile
        #self.object.post_owner = mypost.uploaded_by
        self.object.post = mypost
        self.object.save()
        return HttpResponseRedirect(mypost.get_absolute_url())
        # return HttpResponseRedirect('')
        #return redirect('postdetails', pk = mypost.pk)

# class CommentDelete(DeleteView):
#     model = UserComment
#     #used this method to not confirm just delete (not post just delete and get)
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

    
        
    
#     def get_object(self, queryset=None):
#         """ Hook to ensure object is owned by request.user. """
#         obj = super(CommentDelete, self).get_object()
#         if not obj.comment_by == self.request.user.userprofile:
#             raise Http404
#         return obj

    

def CommentDelete(request, pk):
    comment = get_object_or_404(UserComment, pk=pk)
    if comment.comment_by == request.user.userprofile:
        comment.delete()
    return redirect('postdetails',pk=comment.post.pk)

class UpdateCommentView(UpdateView):
    model = UserComment
    fields = ['comment','c_image']
    def form_valid(self, form):
        mypost = get_object_or_404(UserPost, pk=self.kwargs['pk'])
        self.object = form.save()
        self.object.comment_by = self.request.user.userprofile
        #self.object.post_owner = mypost.uploaded_by
        self.object.post = mypost
        self.object.save()
        return redirect('postdetails', pk = mypost.pk)




# class like_comment(UpdateView):
#     model = UserComment
#     #template_name='olympus/post_details.html'
#     fields = ['cm_likes']
#     def form_valid(self, form):
#         mypost = get_object_or_404(UserPost, pk=self.kwargs['pk'])
#         self.object = form.save()
#         self.object.cm_likes = self.request.user
#         self.object.save()
#         return redirect('postdetails', pk = mypost.pk)



class CommentUpdate(UpdateView):
    model = UserPost
    template_name='olympus/usercomment_update_form.html'
    fields = ['comment','c_image']


class MultipleModelViewForProfilePosts(TemplateView):
    template_name = 'olympus/userpost_form.html'

    def get_context_data(self, **kwargs):

         context = super(MultipleModelViewForProfilePosts, self).get_context_data(**kwargs)
         context['friends_list_p'] = self.request.user.userprofile.friends.all()
         context['all_posts'] = UserPost.objects.filter(uploaded_by=self.request.user.userprofile).order_by('-post_cr_date')
         context['rec_friend_requests'] = FriendRequest.objects.filter(to_user=self.request.user.userprofile).order_by('-id')
        #  context['likes'] = PostLike.objects.all()
         return context


# def MultipleModelViewForProfilePosts(request,id):
#     people = UserProfile.objects.filter(id=id).first()
#     all_posts = UserPost.objects.filter(uploaded_by=request.user.userprofile).order_by('-post_cr_date')
#     friends = people.friends.all()
#     button_status = 'none'
#     if people not in request.user.userprofile.friends.all():
#         button_status = 'not_friend'
#     context = {
		
# 		'button_status': button_status,
# 		'friends_list': friends,
#         'all_posts':all_posts,
# 	}
#     return render(request,'olympus/userpost_form.html',context)



class MultipleModelViewForPostdetails(TemplateView):
    template_name = 'olympus/post_details.html'
    def get_context_data(self, **kwargs):
        context = super(MultipleModelViewForPostdetails, self).get_context_data(**kwargs)
        mypost = get_object_or_404(UserPost, pk=self.kwargs['pk'])
        context['friends_list_p'] = self.request.user.userprofile.friends.all()
        context['post'] = mypost
        context['all_comments'] = UserComment.objects.filter(post=mypost).order_by('-id')
        context['rec_friend_requests'] = FriendRequest.objects.filter(to_user=self.request.user.userprofile).order_by('-id')
        return context



class MultipleModelViewForProfilePhotos(TemplateView):
    template_name = 'olympus/photos.html'
    def get_context_data(self, **kwargs):
         context = super(MultipleModelViewForProfilePhotos, self).get_context_data(**kwargs)
         #mypost = get_object_or_404(UserPost, pk=self.kwargs['pk'])
         #people = UserProfile.objects.filter(id=id).first()
         context['all_posts'] = UserPost.objects.filter(uploaded_by=self.request.user.userprofile).order_by('-post_cr_date')
         context['friends_list_p'] = self.request.user.userprofile.friends.all()
         context['rec_friend_requests'] = FriendRequest.objects.filter(to_user=self.request.user.userprofile).order_by('-id')
         #context['all_comments'] = UserComment.objects.filter(post=mypost).order_by('-id')
         return context

class MultipleModelViewForProfilevideos(TemplateView):
    template_name = 'olympus/videos.html'
    def get_context_data(self, **kwargs):
         context = super(MultipleModelViewForProfilevideos, self).get_context_data(**kwargs)
         #mypost = get_object_or_404(UserPost, pk=self.kwargs['pk'])
        #  def getLength(post_video):
        #      result = subprocess.Popen(["ffprobe", post_video],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        #      context['duration'] = [x for x in result.stdout.readlines() if x.decode()]
         context['all_posts'] = UserPost.objects.filter(uploaded_by=self.request.user.userprofile).order_by('-post_cr_date')
         context['friends_list_p'] = self.request.user.userprofile.friends.all()
         context['rec_friend_requests'] = FriendRequest.objects.filter(to_user=self.request.user.userprofile).order_by('-id')
         #context['all_comments'] = UserComment.objects.filter(post=mypost).order_by('-id')
         return context

# def post_details(request,pk):
#     post = get_object_or_404(UserPost,pk=pk)
#     comments = UserComment.objects.filter(post=post).order_by('-id')
#     context = {
#         'post': post,
#         'all_comments': comments
#     }
#     return render(request,'olympus/post_details.html',context)

class MultipleModelViewForFeeds(TemplateView):
    template_name = 'olympus/newsfeeds.html'
    def get_context_data(self, **kwargs):
        context = super(MultipleModelViewForFeeds, self).get_context_data(**kwargs)
        # people = get_object_or_404(UserProfile, =self.kwargs['pk'])
        # context['all_posts']=UserPost.objects.filter( Q(uploaded_by__friends=self.request.user.userprofile) | Q(uploaded_by=self.request.user.userprofile)).order_by('-id')
        #context['all_posts'] = UserPost.objects.all().order_by('-id')
        context['all_posts']=UserPost.objects.filter( uploaded_by__friends=self.request.user.userprofile).order_by('-id')
        context['inuser'] = UserPost.objects.filter(uploaded_by=self.request.user.userprofile)
        context['friends_list_p'] = self.request.user.userprofile.friends.all()
        context['rec_friend_requests'] = FriendRequest.objects.filter(to_user=self.request.user.userprofile).order_by('-id')
        return context






def get_success_url(self):
    return reverse ('postdetails', kwargs={'pk': self.object.parent.pk})


def like_postinpro(request,pk):
    post = get_object_or_404(UserPost, pk=pk)
    is_liked =False 
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True
    return redirect('/postlist/')

def like_postinPeoplePro(request,id):
    post = get_object_or_404(UserPost, id=id)
    is_liked =False 
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True
    return redirect('showresult',id=post.uploaded_by.id)

def like_post(request,pk):
    post = get_object_or_404(UserPost, pk=pk)
    is_liked =False 
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True
    return redirect('/newsfeeds/')
    # return HttpResponseRedirect('/postdetails/{}/')
 

def like_postindv(request,pk):
    post = get_object_or_404(UserPost, pk=pk)
    is_liked =False 
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True
    return redirect(post.get_absolute_url())
    #return redirect('postdetails',pk=post.pk)

def like_comment(request,pk):
    comment = get_object_or_404(UserComment, pk=pk)
    is_liked =False
    if comment.cm_likes.filter(id=request.user.id).exists():
        comment.cm_likes.remove(request.user)
        is_liked=False
    else:
        comment.cm_likes.add(request.user)
        is_liked=True
    #post = get_object_or_404(UserPost,pk=pk)
    return redirect('postdetails',pk=comment.post.id)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        # slug = self.kwargs.get("slug")
        post = get_object_or_404(UserPost, pk=pk)
        updated = False
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            liked = True
            post.likes.add(request.user)        
        updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)

        


        
# def liking(request, pk):
#     userpost = get_object_or_404(UserPost, pk=pk)
#     obj = PostLike.objects.all()
#     if obj.user.filter(id=request.user.userprofile.id).exists():
#         print('user already exists which likes this')
#         obj.user.delete()
#     else:
#         print('user likes this')
#         newlike = PostLike.objects.create(user=request.user.userprofile, post=userpost)
#     return redirect('/postlist/')


