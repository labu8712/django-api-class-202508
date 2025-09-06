from django.urls import include, path
from rest_framework.routers import DefaultRouter

from server.apps.playground.views import (
    HiView,
    ItemCommentViewSet,
    ItemDetailView,
    ItemListView,
    ItemViewSet,
    hello,
)

router = DefaultRouter(trailing_slash=False)  # 產生 router 並註明不要有結尾的 "/"
# router.register 產生 "items-v2" 跟 "items-v2/<int:pk>" 這兩個路徑到 router.urls 中
router.register("items-v2", ItemViewSet)
router.register("item-comments", ItemCommentViewSet)

urlpatterns = [
    path("hello", hello),
    path("hi", HiView.as_view()),
    path("items", ItemListView.as_view()),
    path("items/<int:item_id>", ItemDetailView.as_view()),
    path("viewset/", include(router.urls)),
]
