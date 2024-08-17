from django.shortcuts import render
from .models import SiteSettings

# Create your views here.


def settings_view(request):
    settings = SiteSettings.objects.first()
    return render(request, 'app_configuracion/settings.html', {'settings': settings})
