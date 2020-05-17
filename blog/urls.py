from django.urls import path
from .views import about,home,contact,blog_single,list_view


app_name = 'blog'

urlpatterns = [
    path('', home,name="home"),
    path('about/', about,name="about"),
    path('contact/', about,name="contact"),
    path('list/<str:list_tag>/', list_view,name="list"),
    path('single/<slug:slug>/<int:id>/', blog_single,name="single"),
    
]