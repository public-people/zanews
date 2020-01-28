from django.db import models
from django_extensions.db.models import TimeStampedModel


class Publication(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)


class Article(TimeStampedModel):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    body_html = models.TextField(blank=True, help_text="The raw original HTML. Kept to be able to re-extract plain text if needed")
    body_text = models.TextField(blank=True, db_index=True)
    byline = models.TextField(bank=True)
    file_name = models.TextField()
    published_at = models.DateTimeField()
    retrieved_at = models.DateTimeField()
    spider_name = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=2048, unique=True)
