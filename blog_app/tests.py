import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User, Post, Comentario, Categoria
from .serializers import UserSerializer, PostSerializer, ComentarioSerializer, CategoriaSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    return User.objects.create(username='testuser', email='test@example.com')

@pytest.fixture
def authenticated_client(api_client, test_user):
    token = Token.objects.create(user=test_user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client

@pytest.mark.django_db
def test_user_viewset(authenticated_client, test_user):
    response = authenticated_client.get('/api/users/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['username'] == test_user.username
    assert response.data[0]['email'] == test_user.email


@pytest.mark.django_db
def test_post_viewset(authenticated_client):
    user = User.objects.get(id=1)
    create_categoria = Categoria.objects.create(nombre="Tests")

    post_data = {'titulo': 'Test Post', 'contenido': 'This is a test post', 'autor': user}
    post = Post.objects.create(**post_data)

    post.categoria.add(create_categoria)

    response = authenticated_client.get('/api/posts/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    serializer = PostSerializer(instance=post)
    assert response.data[0] == serializer.data


@pytest.mark.django_db
def test_comentario_viewset(authenticated_client):
    user = User.objects.get(id=1)
    post = Post.objects.create(titulo='Test Post', contenido='This is a test post', autor=user)

    comentario_data = {'contenido': 'Test Comment', 'post': post.id, 'usuario':user.id} # type: ignore
    response = authenticated_client.post('/api/comentarios/', comentario_data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED

    comentario_id = response.data['id']
    comentario = Comentario.objects.get(id=comentario_id)

    assert comentario.contenido == comentario_data['contenido']
@pytest.mark.django_db
def test_categoria_viewset(authenticated_client):
    categoria_data = {'nombre': 'Test Categoria'}
    response = authenticated_client.post('/api/categorias/', categoria_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED

    categoria_id = response.data['id']
    categoria = Categoria.objects.get(id=categoria_id)

    assert categoria.nombre == categoria_data['nombre']