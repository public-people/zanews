from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from . import models
from .filters import FullTextSearchFilter
from .serializers import ArticleSerializer, PublicationSerializer


class Index(generic.TemplateView):
    template_name = "articles/index.html"


class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.Publication.objects.all()
    serializer_class = PublicationSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, FullTextSearchFilter]
