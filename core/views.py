from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import Article, Project, KindWord

# Create your views here.

def home(request):

    work = Project.objects.filter(project_category=0)

    personal = Project.objects.filter(project_category=1)

    context = {
        'work_projects': work,
        'personal_projects': personal,
    }

    return render(request, 'core/index.html', context)

def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        context = {
            'name': name,
            'email': email,
            'message': message,
        }

        subject = 'New message. Important.'

        from_email = settings.EMAIL_HOST_USER 

        to = settings.RECIPIENT_ADDRESS

        text_content = 'New message from freedom.io. Someone wants to connect.'

        html_content = render_to_string('core/email_notification.html', context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.success(request, 'Your message has been sent successfully.')

    return render(request, 'core/contact.html')

def articles(request):

    all_articles = Article.objects.filter(status=1)

    context = {
        'articles': all_articles,
    }

    return render(request, 'core/all_articles.html', context)

def open_article(request, slug):

    this_article = Article.objects.get(slug = slug)

    context = {
        'article': this_article,
    }

    return render(request, 'core/this_article.html', context)

def about_me(request):

    return render(request, 'core/about.html')

def project_details(request, slug):

    this_project = Project.objects.get(slug=slug)

    is_personal_project = True

    context = {
        'project': this_project,
        'is_personal': is_personal_project,
    }

    return render(request, 'core/this_project.html', context)

def testimonials(request):

    comments = KindWord.objects.all()

    context = {
        'kind_words': comments,
    }

    return render(request, 'core/testimonials.html', context)