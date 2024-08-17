from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_blog.urls')),  # Esta es la ruta principal
    path('usuarios/', include('app_usuarios.urls')),
    path('mensajes/', include('app_mensajes.urls')),
]



