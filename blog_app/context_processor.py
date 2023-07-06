from .models import Categoria,Post,Comentario,Like

def categorias_context_processor(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}

def comentarios_context_processor(request):
    comentarios = Comentario.objects.all()
    cantidad_comentarios = comentarios.count()
    return {'comentarios': comentarios, 'cantidad_comentarios': cantidad_comentarios}

def likes_context_processor(request):
    likes = Like.objects.all()
    cantidad_likes = likes.count()
    return {'likes': likes, 'cantidad_likes': cantidad_likes}