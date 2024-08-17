from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),  # Página "About Us"
    path('contact/', views.contact, name='contact'),  # Página "Contact Us"
    path('<slug:slug>/', views.page_detail, name='page_detail'),  # Visualización de una página estática
]
