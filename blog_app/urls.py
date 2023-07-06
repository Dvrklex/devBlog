from django.urls import path,include
from markdownx import urls as markdownx_urls

from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('ayuda/', views.ayuda, name='Ayuda'),
    path('blog/', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='Categoria'),
    path('post/<int:post_id>/', views.view_post, name='Post'),
    path('my-posts/',views.my_posts,name='MyPosts'),
    path('create_post', views.create_post, name='Create_Post'),
    path('markdownx/', include(markdownx_urls)),
    path('delete-post/<int:post_id>',views.delete_post,name='deletePost'),
    path('edit-post/<int:post_id>',views.edit_post,name='editPost'),
        path('post/<int:post_id>/like/', views.like_post, name='like_post'),



    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 