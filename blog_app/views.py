from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

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

def ayuda(request):
    view_name = 'Ayuda'
    context = {
        "ayuda_css":'blog_app/css/ayuda.css'
    }
    return render(request,'blog_app/ayuda.html',{'view_name':view_name,'context':context})

def blog (request):
    view_name='Blog'
    context = {
        "blog_css":"blog_app/css/blog.css",
        "pagination_css":"blog_app/css/pagination.css",
    }
    
    posts = Post.objects.all().order_by('-created')
    paginator = Paginator(posts,12)
    page = request.GET.get('pagina')
    page_object = paginator.get_page(page)
    
    return render(request,'blog_app/blog.html',{'view_name':view_name,'context':context,'posts':posts,'page_object':page_object})

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



# View My posts
@login_required
def my_posts(request):
    view_name = 'Mis Posts'
    context = {
        "userPosts": "blog_app/css/user_posts.css",
    }

    user = request.user
    posts = Post.objects.filter(autor=user).order_by('-created')
    paginator = Paginator(posts, 12)
    page = request.GET.get('pagina')
    page_object = paginator.get_page(page)

    return render(request, 'blog_app/user_posts.html', {
        'view_name': view_name,
        'context': context,
        'posts': posts,
        'page_object': page_object
    })
  
  
## Create Post
def create_post(request):
    view_name = 'Create_Post'
    context = {
        "css_file": "blog_app/css/create_post.css",
    }
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        introduccion = request.POST.get('introduccion')
        categoria_id = request.POST.get('categoria')
        contenido = request.POST.get('contenido')
        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id)
        imagen = request.FILES.get('imagen')
        autor = request.user

        if imagen and imagen.size > settings.MAX_UPLOAD_SIZE:
            error_message = 'La imagen es demasiado grande. El tamaño máximo permitido es de 5 MB.'
            return render(request, 'blog_app/create_post.html', {
                'view_name': view_name,
                'context': context,
                'categorias': categorias,
                'error_message': error_message,
                'titulo': titulo,
                'categoria_id': int(categoria_id),
                'contenido': contenido
            })
        else:
            post = Post(titulo=titulo,introduccion=introduccion, contenido=contenido, imagen=imagen, autor=autor)
            post.save()
            post.categoria.set([categoria])
            return redirect('Blog')

    return render(request, 'blog_app/create_post.html', {
        'view_name': view_name,
        'context': context,
        'categorias': categorias
    })
    
## Delete post
@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('MyPosts') 
   
   
# Edit Post
@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    view_name = 'Edit_Post'
    context = {
        "css_file": "blog_app/css/create_post.css",
    }
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        post.titulo = request.POST.get('titulo', post.titulo)
        post.introduccion = request.POST.get('introduccion', post.introduccion)
        post.contenido = request.POST.get('contenido', post.contenido)
        
        categoria_id = request.POST.get('categoria')
        if categoria_id:
            categoria = Categoria.objects.get(id=categoria_id)
            post.categoria.set([categoria])

        imagen = request.FILES.get('imagen')
        if imagen and imagen.size > settings.MAX_UPLOAD_SIZE:
            error_message = 'La imagen es demasiado grande. El tamaño máximo permitido es de 5 MB.'
            return render(request, 'blog_app/edit_post.html', {
                'view_name': view_name,
                'context': context,
                'post': post,
                'categorias': categorias,
                'error_message': error_message
            })
        elif imagen:
            post.imagen = imagen

        post.save()
        return redirect('MyPosts')

    return render(request, 'blog_app/edit_post.html', {
        'view_name': view_name,
        'context': context,
        'post': post,
        'categorias': categorias
    })
