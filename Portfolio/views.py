from django.shortcuts import render
from django.core.mail import send_mail
import environ
# Initialize environment variables
env = environ.Env(DEBUG=(bool, False))
env.read_env( '.env')  # Reads the .env file
# Create your views here.
from .models import Project, Skills, Personal, SocialLinks

def portfolio(request):
    projects = Project.objects.all()  # Fetch all projects
    skills = Skills.objects.all()
    personal = Personal.objects.all()
    socialinks = SocialLinks.objects.all()
    #Function SMTP Email
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Contact from {name}"
        
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        email_from = email
        recipient_list = [env('EMAIL_HOST_USER')]
        send_mail(subject, email_message, email_from, recipient_list)
    return render(
        request,
        "portfolio/index.html",
        {
            'projects': projects,
            'skills':skills,
            'personal':personal,
            'socialinks':socialinks
        }
        )