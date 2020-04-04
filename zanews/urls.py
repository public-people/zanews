from django.contrib import admin
from django.urls import include, path

from . import views
from .articles.urls import api_router

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("articles", include("zanews.articles.urls"),),
    path("api/", include(api_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
