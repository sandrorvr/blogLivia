from django.urls import path
from blog.views import single, index, about, article


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('single/', single, name='single'),
    path('single/<int:art>', article, name='article'),
]