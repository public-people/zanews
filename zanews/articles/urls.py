from django.urls import include, path
from rest_framework import routers
from . import views


api_router = routers.DefaultRouter()
api_router.register(r"publications", views.PublicationViewSet)
api_router.register(r"articles", views.ArticleViewSet)


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
]
