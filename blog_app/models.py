from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)  
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre 
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    introduccion = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='post', null=True) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  
    categoria = models.ManyToManyField(Categoria) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.titulo} creado por {self.autor.username}'
   
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.post.titulo}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self):
        return f"Like de {self.usuario.username} en {self.post.titulo}"