from django.contrib import admin

from blog.models import Posts, PostDetail, Profile

admin.site.register(Posts)
admin.site.register(PostDetail)
admin.site.register(Profile)