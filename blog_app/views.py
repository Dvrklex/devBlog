from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    view_name= 'Home' 
    context = {
        "home_css":"blog_app/css/home.css",
        }
    latest_posts = Post.objects.all().order_by('-created')[:3]
    print(latest_posts)
    return render(request, 'blog_app/home.html',{'view_name': view_name,"context":context,"latest_posts":latest_posts})
