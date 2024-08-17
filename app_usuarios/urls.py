from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Página de registro
    path('login/', CustomLoginView.as_view(), name='login'),  # Página de login
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Página de logout
    path('profile/', views.profile, name='profile'),  # Perfil del usuario actual
    path('profile/<int:pk>/', profile_detail, name='profile_detail'),  # Ver perfil de otro usuario
]
