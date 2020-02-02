from rest_framework import serializers

from . import models


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Publication
        fields = ["name", "slug", "url"]
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Article
        fields = [
            "body_html",
            "byline",
            "file_name",
            "publication",
            "published_at",
            "retrieved_at",
            "spider_name",
            "title",
            "published_url",
            "url",
        ]
        extra_kwargs = {
            "body_html": {"write_only": True},
            "publication": {"lookup_field": "slug"},
        }
