from django.shortcuts import render
from .models import Post,Categoria
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

def categoria(request,categoria_id):
    view_name='Categoria'
    context = {
        "blog_css":"blog_app/css/blog.css",
        "categoria_css":"blog_app/css/categoria.css",
    }
    
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    
    return render(request,'blog_app/filtro_categoria.html',{'view_name':view_name,'context':context,'categoria':categoria,'posts':posts})


#View one post 
def view_post(request, post_id): 
    view_name = 'View_post'
    context = {
        "post_css":"blog_app/css/post.css",
        "post_js":"blog_app/js/post.js",
        
        }
    post = Post.objects.get(id=post_id)
    return render(request, 'blog_app/post.html', {'view_name':view_name,"context":context ,'post': post})

