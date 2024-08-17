from django.urls import path
from . import views
from app_blog.views import about

urlpatterns = [
    path('', views.index, name='index'),  # Página principal del blog
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_form, name='post_form'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_confirm_delete, name='post_confirm_delete'),
    path('about/', views.about, name='about'),  # Página "About Us"
    path('contact/', views.contact, name='contact'),  # Página "Contact Us"
    path('<slug:slug>/', views.page_detail, name='page_detail'),  # Visualización de una página estática
]
