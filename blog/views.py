from django.shortcuts import render
from blog.models import Posts, PostDetail, Profile
def index(request):
    context = {
        'profile': Profile.objects.all()[0],
        'posts': Posts.objects.all()
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')