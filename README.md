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

1. Clona el repositorio.
2. Ejecuta `python3 manage.py runserver`.
3. Instala los requerimientos `pip install -r requirements.txt`.
   a. Django
   b. Markdown
   c. Markdownx
5. La base de datos es SQLite3 y se ejecutan las migraciones con `python3 manage.py migrate`.

Requisitos: tener instalado Django y Python. La única librería adicional a instalar es ckeditor widget.

Inicia el proyecto con el comando `python3 manage.py runserver` y abre el navegador en http://localhost:8000


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
        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-plain.svg"
        width="48"
        height="48"
        alt="JavaScript"
      />
      <br /><strong>JavaScript</strong>
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
