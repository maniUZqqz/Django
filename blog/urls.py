from django.urls import path
from . import views




urlpatterns = [
    path('', views.blog, name='blog'),
    path('all_post/', views.all_post, name='all_post'),
    path('post/<slug:slug>', views.single_post, name='single_post'),
]





# <a href="{% url 'single_post' slug=post.slug %}">post</a>