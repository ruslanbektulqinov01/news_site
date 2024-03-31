from django.test import TestCase

from articles.models import Article
from articles.views import *

class ArticleModelTestCase(TestCase):
    def test_article_str_representation(self):
        article = Article(title="Sample Title", author="John Doe")
        self.assertEqual(str(article), "Sample Title")


class ArticleAllViewTestCase(TestCase):
    
    def test_article_all_view(self):
        Article.objects.create(title="Test Article", author="John Doe", description="Sample description")
        response = self.client.post(reversed('articles'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form', count=1)
        self.assertContains(response, 'Test Article')

    def test_article_all_view_no_articles(self):
        response = self.client.get(reversed('articles'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form', count=1)
        self.assertContains(response, 'No articles found.')