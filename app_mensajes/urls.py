from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),  # Bandeja de entrada
    path('send/', views.send_message, name='send_message'),  # Enviar un mensaje
]
