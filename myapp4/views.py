# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def send_email(request):
    if request.method == 'POST':
        send_mail(
            'Welcome Party - reg.',
            'Greetings!!! Welcome to the Department of Information Technology.',
            settings.EMAIL_HOST_USER,
            ['janavarshini21@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'sendMail.html')  # Redirect to sendMail.html after sending the email
    return render(request, 'home.html')  # Return to home if not POST
