from django.urls import path
from . import views
from .views import ViewRegistro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', ViewRegistro.as_view(), name='SignUp'),
    path('login', views.login_view, name='Login'),
    path('logout', views.cerrar_sesion, name='Logout'),
   
]

#Leer las imagenes de la carpeta media en el navegador
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)