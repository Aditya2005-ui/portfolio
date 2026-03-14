from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Portfolio message from {name}"

        full_message = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=True
        )

        return redirect("/")

    return render(request, "home.html")