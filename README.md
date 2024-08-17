PFinal-KSE
Este es un proyecto Django llamado PFinal-KSE. El proyecto está estructurado con varias aplicaciones que cubren diferentes funcionalidades, como la gestión de un blog, manejo de usuarios, envío de mensajes, y páginas estáticas.

Estructura del Proyecto
El proyecto contiene las siguientes aplicaciones:

app_blog: Gestiona las publicaciones del blog, incluyendo la creación, edición, y eliminación de posts.
app_usuarios: Maneja el registro, inicio de sesión, perfiles de usuario y autenticación.
app_mensajes: Soporta el envío y recepción de mensajes entre usuarios.
app_paginas: Contiene páginas estáticas como 'About' y 'Contact'.
app_base: Provee las plantillas base y archivos estáticos comunes (CSS, JS, imágenes) utilizados en todo el proyecto.
Requisitos
Python 3.12
Django 5.0.6
Bootstrap 5.2.3 (opcional, si utilizas plantillas Bootstrap)
Instalación
Clona este repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/PFinal-KSE.git
cd PFinal-KSE
Crea un entorno virtual:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Realiza las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate
Crea un superusuario para acceder al panel de administración:

bash
Copiar código
python manage.py createsuperuser
Inicia el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Accede al proyecto en tu navegador en http://127.0.0.1:8000/.

Funcionalidades
app_blog
Post List: Muestra una lista de todas las publicaciones del blog.
Post Detail: Muestra los detalles de una publicación específica.
Post Create: Permite a los usuarios crear nuevas publicaciones (solo para usuarios autenticados).
Post Edit: Permite editar publicaciones existentes.
Post Delete: Permite eliminar publicaciones existentes.
app_usuarios
Registro: Los usuarios pueden registrarse en el sitio.
Inicio de sesión: Los usuarios registrados pueden iniciar sesión.
Perfil de usuario: Los usuarios pueden ver y editar su perfil.
Logout: Los usuarios pueden cerrar sesión.
app_mensajes
Enviar mensaje: Permite a los usuarios enviar mensajes privados a otros usuarios.
Lista de mensajes: Los usuarios pueden ver los mensajes recibidos y enviados.
app_paginas
Página de inicio: Muestra un resumen del sitio.
About: Página estática con información sobre el sitio.
Contact: Formulario de contacto para que los usuarios se comuniquen con los administradores.
app_base
Plantillas base: Estructura HTML común para todas las páginas.
Archivos estáticos: CSS, JS, e imágenes compartidos.
Personalización
Para cambiar la longitud mínima de las contraseñas y otros aspectos de la creación de usuarios, se personalizó el formulario CustomUserCreationForm en app_usuarios/forms.py.

También puedes ajustar las configuraciones de rutas, plantillas, y otros aspectos del proyecto editando los archivos correspondientes en cada aplicación.
