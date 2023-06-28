from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    view_name= 'Home' 
    context = {
        "home_css":"blog_app/css/home.css",
        "slider_css":"blog_app/css/slider.css",
        "swiperBundleCss":"blog_app/css/swiper-bundle.min.css",
        #Scripts 
        "swiperBundleJs":"blog_app/js/swiper-bundle.min.js",
        "sliderJs":"blog_app/js/slider.js",
        }
    latest_posts = Post.objects.all().order_by('-created')[:5]
    print(latest_posts)
    return render(request, 'blog_app/home.html',{'view_name': view_name,"context":context,"latest_posts":latest_posts})


def blog (request):
    view_name='Blog'
    context = {
        "blog_css":"blog_app/css/blog.css",

    }
    
    posts = Post.objects.all().order_by('-created')
    
    return render(request,'blog_app/blog.html',{'view_name':view_name,'context':context,'posts':posts})