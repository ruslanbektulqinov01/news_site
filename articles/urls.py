from django.urls import path
from articles.views import article_all, login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', article_all, name='article_all'),
    path('login/', login, name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
