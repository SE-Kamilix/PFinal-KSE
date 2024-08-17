
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import UserProfile

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'app_usuarios/signup.html', {'form': form})

def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'app_usuarios/profile.html', {'profile': profile})


class CustomLoginView(LoginView):
    template_name = 'app_usuarios/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirigir a la página de login después del logout


def profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'app_usuarios/profile_detail.html', {'profile': profile})
