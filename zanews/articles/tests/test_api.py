from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from zanews.articles import models


class CreatePublicationTests(APITestCase):
    def test_create_publication(self):
        """
        Ensure we can create a new publication object.
        """
        url = reverse("publication-list")
        data = {
            "name": "Wednesday Moon",
            "slug": "whatever-we-want",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Publication.objects.count(), 1)
        self.assertEqual(models.Publication.objects.get().name, "Wednesday Moon")

    def test_anon_create_publication_rejected(self):
        """
        Ensure that AnonymousUser can not create a new publication object.
        """
        url = reverse("publication-list")
        data = {
            "name": "Wednesday Moon",
            "slug": "whatever-we-want",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(models.Publication.objects.count(), 0)


class ArticleTests(APITestCase):
    fixtures = ["api_create_article"]

    def test_create_article(self):
        """
        Ensure we can create a new article object.
        """
        data = {
            "publication": reverse(
                "publication-detail", args=[models.Publication.objects.first().slug]
            ),
            "byline": "Fred Bloggs",
            "body_html": "<p>A page body</p>",
            "file_name": "it-happened.html",
            "published_at": "2001-01-02T03:04:00",
            "retrieved_at": "2002-03-04T05:06:00",
            "spider_name": "wed_moon",
            "title": "It happened!",
            "published_url": "https://example.com/it-happened",
        }
        response = self.client.post(reverse("article-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Article.objects.count(), 1)
        self.assertEqual(models.Article.objects.get().title, "It happened!")

    def test_anon_create_article_rejected(self):
        """
        Ensure that AnonymousUser can not create a new article object.
        """
        url = reverse("article-list")
        data = {
            "publication": reverse(
                "publication-detail", args=[models.Publication.objects.first().slug]
            ),
            "byline": "Fred Bloggs",
            "body_html": "<p>A page body</p>",
            "file_name": "it-happened.html",
            "published_at": "2001-01-02T03:04:00",
            "retrieved_at": "2002-03-04T05:06:00",
            "spider_name": "wed_moon",
            "title": "It happened!",
            "published_url": "https://example.com/it-happened",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(models.Article.objects.count(), 0)
