from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import ArticleForm
from webapp.models import Article


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(data={
            'title': article.title,
            'text': article.text,
            'author': article.author
        })
        return render(request, 'update.html', context={'form': form, 'article': article})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.author = form.cleaned_data['author']
            article.text = form.cleaned_data['text']
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'article': article})


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    return render(request, 'article_view.html', context={
        'article': article
    })


def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'article_create.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text']
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', context={'form': form})

def calc_form_view(request):
    if request.method == 'GET':
        return render(request, 'calc_form.html')
    elif request.method == 'POST':
        context = {
            'num1': request.POST.get('num1'),
            'num2': request.POST.get('num2'),
            'check': request.POST.get('check'),
            'result': request.POST.get('result'),
        }
        if context['check'] == '+':
            context['result'] = int(context['num1']) + int(context['num2'])
        elif context['check'] == '-':
            context['result'] = int(context['num1']) - int(context['num2'])
        elif context['check'] == '*':
            context['result'] = int(context['num1']) * int(context['num2'])
        elif context['check'] == '/':
            context['result'] = int(context['num1']) / int(context['num2'])
        return render(request, 'calc_view.html', context)


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def index1_view(request):
    return render(request, 'index1.html')

