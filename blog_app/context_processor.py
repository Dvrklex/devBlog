from .models import Categoria,Post,Comentario,Like

def categorias_context_processor(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}




