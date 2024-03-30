from django.shortcuts import render, redirect
from articles.models import Article
from articles.forms import ArticleForm


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
        'form': form,
        'maqolalar': maqolalar
    }
    return render(request, 'maqola.html', context=context)
