from django.shortcuts import render
from blog.models import Posts, PostDetail, Profile
def index(request):
    context = {
        'profile': Profile.objects.all()[0],
        'posts': Posts.objects.all()
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'profile': Profile.objects.all()[0],
    }
    return render(request, 'about.html', context)


def single(request):
    context = {
        'profile': Profile.objects.all()[0],
        'detail': PostDetail.objects.all()
    }
    return render(request, 'single.html', context)

def article(request, art):
    context = {
        'profile': Profile.objects.all()[0],
        'detail': PostDetail.objects.get(id=art)
    }
    return render(request, 'article.html', context)
