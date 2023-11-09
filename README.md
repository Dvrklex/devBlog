##  <div align="center">**DEV Blog**</div>

Este proyecto es un blog desarrollado con Django. El propósito principal es poner en práctica varias funcionalidades aprendidas, como context_processors, signals, tests, paginación, filtros, autenticación y personalización/configuración del panel de administración. El blog permite a los usuarios agregar categorías a los posts, dar likes y dejar comentarios en las publicaciones. Además, los usuarios registrados pueden gestionar sus propios posts mediante un CRUD básico.

## <h2 align="center"> Características</h2>
```bash
- Cada post puede tener categorías.
- Los usuarios que hayan iniciado sesión pueden darle like o comentar en el blog.
- Los usuarios pueden gestionar sus propios posts (CRUD).
- Los usuarios pueden ver a qué posts les dieron like.
- Incluye un usuario Administrador para la gestión del proyecto.
	- Usuario: Admin
	- Contraseña: admin
```

## <h2 align="center"> Estructura del proyecto</h2>

La estructura del proyecto sigue la convención generada por Django. Está compuesto por el proyecto principal y dos aplicaciones: `blog` y `user`.

- `blog`: Contiene los modelos, vistas, URLs y plantillas relacionadas con el blog y los posts.
- `user`: Maneja la autenticación de usuarios, registro, inicio de sesión y gestión de usuarios.
  
## <h2 align="center"> Instalación y configuración</h2>


Para instalar y configurar el proyecto en localhost:

*Requisitos: tener instalado Django y Python. La única librería adicional a instalar es ckeditor widget.*
1. Clona el repositorio.
2. Ejecuta `python3 manage.py runserver`.
3. Instala los requerimientos `pip install -r requirements.txt`.
   - Django
   - Markdown
   - Markdownx
5. La base de datos es SQLite3 y se ejecutan las migraciones con `python3 manage.py migrate`.


Inicia el proyecto con el comando `python3 manage.py runserver` y abre el navegador en http://localhost:8000
## <h2 align="center"> Endpoints de la API</h2>

A continuación se describen los principales endpoints de la API con ejemplos de solicitud y respuesta.

### Autenticación

#### Obtener token de autenticación
- **Método**: POST
- **Endpoint**: `/api/token/`
- **Cuerpo de la solicitud**:
    ```json
    {
        "username": "Admin",
        "password": "admin"
    }
    ```
- **Ejemplo de respuesta**:
    ```json
    {
        "token": "tu_token_de_autenticacion"
    }
    ```

### Categorías

#### Obtener todas las categorías
- **Método**: GET
- **Endpoint**: `/api/categorias/`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**:
    ```json
    [
        {
            "id": 1,
            "nombre": "Nombre de la categoria"
        },
        // Otros objetos de categoría
    ]
    ```

#### Obtener una categoría por ID
- **Método**: GET
- **Endpoint**: `/api/categorias/1`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 1,
        "nombre": "Nombre de la categoria"
    }
    ```

#### Crear una nueva categoría
- **Método**: POST
- **Endpoint**: `/api/categorias/`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud**:
    ```json
    {
        "nombre": "Nueva Categoria"
    }
    ```
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 2,
        "nombre": "Nueva Categoria"
    }
    ```

#### Actualizar una categoría por ID
- **Método**: PUT
- **Endpoint**: `/api/categorias/1`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud**:
    ```json
    {
        "nombre": "Nuevo nombre"
    }
    ```
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 1,
        "nombre": "Nuevo nombre"
    }
    ```

#### Eliminar una categoría por ID
- **Método**: DELETE
- **Endpoint**: `/api/categorias/1`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**: 204 No Content

### Comentarios

#### Obtener todos los comentarios
- **Método**: GET
- **Endpoint**: `/api/comentarios/`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**:
    ```json
    [
        {
            "id": 1,
            "contenido": "Contenido del nuevo comentario",
            "post": 1,
            "usuario": 1
        },
        // Otros objetos de comentario
    ]
    ```

#### Obtener un comentario por ID
- **Método**: GET
- **Endpoint**: `/api/comentarios/1`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 1,
        "contenido": "Contenido del nuevo comentario",
        "post": 1,
        "usuario": 1
    }
    ```

#### Crear un nuevo comentario
- **Método**: POST
- **Endpoint**: `/api/comentarios/`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud**:
    ```json
    {
        "contenido": "Contenido del nuevo comentario",
        "post": 1,
        "usuario": 1
    }
    ```
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 2,
        "contenido": "Contenido del nuevo comentario",
        "post": 1,
        "usuario": 1
    }
    ```

#### Eliminar un comentario por ID
- **Método**: DELETE
- **Endpoint**: `/api/comentarios/2`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**: 204 No Content

### Posts

#### Obtener todos los posts
- **Método**: GET
- **Endpoint**: `/api/posts/`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**:
    ```json
    [
        {
            "id": 1,
            "titulo": "titulo",
            "introduccion": "introduccion",
            "contenido": "Post creado desde postman",
            "autor": 1,
            "categoria": [1]
        },
        // Otros objetos de post
    ]
    ```

#### Obtener un post por ID
- **Método**: GET
- **Endpoint**: `/api/posts/1`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 1,
        "titulo": "titulo",
        "introduccion": "introduccion",
        "contenido": "Post creado desde postman",
        "autor": 1,
        "categoria": [1]
    }
    ```

#### Crear un nuevo post
- **Método**: POST
- **Endpoint**: `/api/posts/`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud**:
    ```json
    {
        "titulo": "titulo",
        "introduccion": "introduccion",
        "contenido": "Post creado desde postman",
        "autor": 1,
        "categoria": [1]
    }
    ```
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 2,
        "titulo": "titulo",
        "introduccion": "introduccion",
        "contenido": "Post creado desde postman",
        "autor": 1,
        "categoria": [1]
    }
    ```

#### Actualizar un post por ID
- **Método**: PUT
- **Endpoint**: `/api/posts/1`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud**:
    ```json
    {
        "titulo": "Nuevo titulo",
        "introduccion": "Nueva introduccion",
        "contenido": "Nuevo contenido",
        "categoria": [2]
    }
    ```
- **Ejemplo de respuesta**:
    ```json
    {
        "id": 1,
        "titulo": "Nuevo titulo",
        "introduccion": "Nueva introduccion",
        "contenido": "Nuevo contenido",
        "autor": 1,
        "categoria": [2]
    }
    ```

#### Eliminar un post por ID
- **Método**: DELETE
- **Endpoint**: `/api/posts/2`
- **Cabecera de la solicitud**: `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta**: 204 No Content

## <h2 align="center"> Pruebas con Pytest</h2>

Para ejecutar las pruebas con Pytest, sigue estos pasos:

1. Asegúrate de tener Pytest instalado (`pip install pytest`).
2. Ejecuta el siguiente comando en el directorio del proyecto:
    ```bash
    pytest
    ```
3. Observa la salida de la consola para ver los resultados de las pruebas.


## <h2 align="center">Tecnologías utilizadas</h2>
<div align="center">
<table>
  <tr>
    <td align="center" height="108" width="108">
      <img
        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain.svg"
        width="48"
        height="48"
        alt="HTML"
      />
      <br /><strong>HTML5</strong>
    </td>
    <td align="center" height="108" width="108">
      <img
        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain.svg"
        width="48"
        height="48"
        alt="CSS3"
      />
      <br /><strong>CSS3</strong>
    </td>
    <td align="center" height="108" width="108">
      <img
        src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"
        width="48"
        height="48"
        alt="Pytest"
      />
      <br /><strong>Pytest</strong>
    </td>
    <td align="center" height="108" width="108">
      <img
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png"
        width="48"
        height="48"
        alt="PYTHON"
      />
      <br /><strong>Python</strong>
    </td>
    <td align="center" height="108" width="108">
      <img
        src="https://icon.icepanel.io/Technology/png-shadow-512/Django-REST.png"
        width="48"
        height="48"
        alt="Django Rest"
      />
      <br /><strong>Django Rest</strong>
    </td>
    <td align="center" height="108" width="108">
      <img
        src="https://profilinator.rishav.dev/skills-assets/django-original.svg"
        width="48"
        height="48"
        alt="Django"
      />
      <br /><strong>Django</strong>
    </td>

    
    
 </tr>
</table>

  </div>





<h1></h1>
<br>
<p align="center">¡Gracias por visitar este proyecto!</p>
