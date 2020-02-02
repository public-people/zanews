from bs4 import BeautifulSoup
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from rest_framework.authtoken.models import Token

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

    class Meta:
        ordering = ["name"]


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
    published_at = models.DateTimeField(db_index=True)
    retrieved_at = models.DateTimeField()
    spider_name = models.CharField(max_length=50)
    title = models.CharField(max_length=300, db_index=True)
    published_url = models.CharField(max_length=2048, unique=True)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        soup = BeautifulSoup(self.body_html, "html.parser")
        self.body_text = ""

        for t in soup.find_all(text=True):
            if t.parent.name not in TAG_BLACKLIST:
                self.body_text += "{} ".format(t)
        super().save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
