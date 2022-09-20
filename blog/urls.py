from django.urls import path
from blog.views import index, about


urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='about'),
]