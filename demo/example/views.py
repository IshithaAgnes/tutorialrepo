from django.shortcuts import render,redirect
from rest_framework import viewsets

from .forms import ArticleForm
from .models import Article, MyModel
from .serializers import MyModelSerializer


def home(request):
    return render(request,"home.html")

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer