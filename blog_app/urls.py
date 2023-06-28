from django.urls import path

from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='Categoria'),
        path('post/<int:post_id>/', views.view_post, name='Post'),

    # path('autor/<int:autor_id>/', views.autor, name='Autor'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 