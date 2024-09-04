from django.shortcuts import render
from dashboard.models import Articles

def home(request):
    articles = Articles.objects.all().order_by('-date')[:3]
    return render(request, "index.html", {'articles': articles})

def about(request):
    return render(request, "about.html")


def dechets(request):
    return render(request, "dechets.html")

def reseau(request):
    return render(request, "reseau.html")

def services(request):
    return render(request, "services.html")

def news(request):
    articles = Articles.objects.all().order_by('-date')
    return render(request, "blog.html", {"articles" : articles})

def news_details(request, id):
    articles = Articles.objects.all().order_by('-date')[:6]
    article = Articles.objects.get(pk=id)
    return render(request, "blog-details.html", {"article" : article, "articles" : articles})

def contact(request):
    return render(request, "contact.html")