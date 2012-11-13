from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext_lazy as _

from core.decorators import admin_required_decorator

from .forms import ArticleForm
from .models import Article



def home(request):
    data = {'articles': Article.published_query().order('-publish_date')}
    return request.render('article/home.html', data)


@admin_required_decorator
def list_articles(request):
    data = {'articles': Article.all().order('-publish_date')}
    return request.render('article/list.html', data)


@admin_required_decorator
def add_edit(request, key=None):
    instance = Article.get(key) if key else None
    form = ArticleForm(instance, request.POST or None)
    if form.is_valid():
        article_key = form.save()
        if article_key:
            messages.success(request, _(u'Article saved successfully'))
            return HttpResponseRedirect(reverse('edit-article', kwargs={'key': article_key}))
    return request.render('article/edit.html', {'form': form})


def single_article(request, slug):
    article = Article.published_query().filter('slug =', slug).get()
    if not article:
        raise Http404
    return request.render('article/single_article.html', {'article': article})


@admin_required_decorator
def delete_article(request, key):
    article = Article.get(key)
    if not article:
        raise Http404
    if request.POST:
        article.delete()
        return HttpResponseRedirect(reverse('list-articles'))
    else:
        return request.render('article/delete_article.html',
                              {'article': article})
