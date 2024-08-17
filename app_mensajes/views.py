from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'app_mensajes/inbox.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        recipient = User.objects.get(username=request.POST['recipient'])
        message = Message(
            sender=request.user,
            recipient=recipient,
            body=request.POST['body']
        )
        message.save()
        return redirect('inbox')
    return render(request, 'app_mensajes/send_message.html')
