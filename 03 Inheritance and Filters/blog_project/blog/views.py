from django.shortcuts import render
from .models import Article
# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles':articles})

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')