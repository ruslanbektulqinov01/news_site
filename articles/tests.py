from django.test import TestCase

# Create your tests here.
# tests.py

from articles.models import Article

class ArticleModelTestCase(TestCase):
    def test_article_str_representation(self):
        article = Article(title="Sample Title", author="John Doe")
        self.assertEqual(str(article), "Sample Title")

    # Add more test methods as needed

# tests.py

class ArticleModelTestCase(TestCase):
    def test_article_str_representation(self):
        article = Article(title="Sample Title", author="John Doe")
        self.assertEqual(str(article), "Sample Title")

    # Add more test methods as needed
class ArticleAllViewTestCase(TestCase):
    def test_article_all_view(self):
        # Create a sample article
        Article.objects.create(title="Test Article", author="John Doe", description="Sample description")

        # Simulate a POST request to the view
        response = self.client.post(reversed('articles'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the form is rendered
        self.assertContains(response, '<form', count=1)

        # Check if the article is displayed
        self.assertContains(response, 'Test Article')

    def test_article_all_view_no_articles(self):
        # Simulate a GET request to the view
        response = self.client.get(reversed('articles'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the form is rendered
        self.assertContains(response, '<form', count=1)

        # Check if no articles are displayed
        self.assertContains(response, 'No articles found.')

    # Add more test methods as needed

