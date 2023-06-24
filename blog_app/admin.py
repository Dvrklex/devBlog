from django.contrib import admin
from .models import Categoria, Post, Comentario, Like

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('nombre',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'get_categorias', 'created', 'updated')
    list_filter = ('autor', 'categoria', 'created', 'updated')
    search_fields = ('titulo', 'autor__username', 'categoria__nombre')
    filter_horizontal = ('categoria',)

    def get_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categoria.all()])
    get_categorias.short_description = 'Categorías'

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'usuario', 'contenido', 'created')
    list_filter = ('created',)
    search_fields = ('post__titulo', 'usuario__username', 'contenido')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'usuario', 'created')
    list_filter = ('created',)
    search_fields = ('post__titulo', 'usuario__username')
