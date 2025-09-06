from django.urls import include, path
from rest_framework.routers import DefaultRouter

from server.apps.playground.views import (
    HiView,
    ItemDetailView,
    ItemListView,
    ItemViewSet,
    hello,
)

router = DefaultRouter(trailing_slash=False)
router.register("items-v2", ItemViewSet)

urlpatterns = [
    path("hello", hello),
    path("hi", HiView.as_view()),
    path("items", ItemListView.as_view()),
    path("items/<int:item_id>", ItemDetailView.as_view()),
    path("viewset/", include(router.urls)),
]
