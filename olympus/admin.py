
from django.contrib import admin
from .models import UserPost,PostLike,UserComment

class PostAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'post_write', 'post_image','post_cr_date')
admin.site.register(UserPost, PostAdmin)


class LikedAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'cr_date')
admin.site.register(PostLike, LikedAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_by','comment','c_image','cm_cr_date')
admin.site.register(UserComment, CommentAdmin)

# admin.site.register(UserComment)
# Register your models here.


