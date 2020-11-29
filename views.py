from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleScopes


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.order_by('-published_at')
    article_topics = ArticleScopes.objects.all()
    context = {'object_list': object_list, 'scopes': article_topics}
    return render(request, template, context)
