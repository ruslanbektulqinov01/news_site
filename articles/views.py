from django.shortcuts import render, redirect
from articles.models import Article
from articles.forms import ArticleForm


# from django.http import Http404
def article_all(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm()

    maqolalar = Article.objects.all().order_by('-id')
    context = {
        'maqolalar': maqolalar,
        'form': form
    }
    return render(request, 'maqola.html', context=context)


def login(request):
    return render(request, 'auth/login.html')


def custom_404(request):
    return render(request, '404.html', status=404)
