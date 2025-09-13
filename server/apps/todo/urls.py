from django.urls import include, path
from rest_framework.routers import DefaultRouter

from server.apps.todo.views import ProjectViewSet, TagViewSet, TaskViewSet

router = DefaultRouter(trailing_slash=False)
router.register("projects", ProjectViewSet)
router.register("tags", TagViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
