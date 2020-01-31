from django.db import models
from django_extensions.db.models import TimeStampedModel
from bs4 import BeautifulSoup


TAG_BLACKLIST = {
    "[document]",
    "noscript",
    "header",
    "html",
    "meta",
    "head",
    "input",
    "script",
    "style",
}


class Publication(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class Article(TimeStampedModel):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    body_html = models.TextField(
        blank=True,
        help_text=(
            "The raw original HTML."
            " Kept to be able to re-extract plain text if needed"
        ),
    )
    body_text = models.TextField(blank=True, db_index=True)
    byline = models.TextField(blank=True)
    file_name = models.TextField()
    published_at = models.DateTimeField()
    retrieved_at = models.DateTimeField()
    spider_name = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    published_url = models.CharField(max_length=2048, unique=True)

    def save(self, *args, **kwargs):
        soup = BeautifulSoup(self.body_html, "html.parser")
        self.body_text = ""

        for t in soup.find_all(text=True):
            if t.parent.name not in TAG_BLACKLIST:
                self.body_text += "{} ".format(t)
        super().save(*args, **kwargs)
