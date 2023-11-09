from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from blog_app import view_set
router = DefaultRouter()
router.register(r'users', view_set.UserViewSet)
router.register(r'posts', view_set.PostViewSet)
router.register(r'comentarios', view_set.ComentarioViewSet)
router.register(r'categorias',view_set.CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api/token/', obtain_auth_token, name='api_token'), 
    path('', include('blog_app.urls')), 
    path('', include('user.urls')), 
   ]