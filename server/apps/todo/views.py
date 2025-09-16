from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from server.apps.todo.models import Project, Tag, Task
from server.apps.todo.permissions import IsOwner
from server.apps.todo.serializers import (
    ProjectSerializer,
    TagSerializer,
    TaskSerializer,
)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.select_related("owner")
    serializer_class = ProjectSerializer

    ordering_fields = ["id", "created_at", "updated_at"]
    ordering = ["-created_at"]

    search_fields = ["name"]

    filterset_fields = {
        "id": ["gt", "gte", "lt", "lte"],
        "created_at": ["gt", "gte", "lt", "lte"],
        "updated_at": ["gt", "gte", "lt", "lte"],
        "name": ["exact", "contains"],
        "is_public": ["exact"],
        "owner": ["exact"],
    }

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(Q(owner=self.request.user) | Q(is_public=True))
        )


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.select_related("owner")
    serializer_class = TagSerializer

    ordering_fields = ["id", "created_at", "updated_at"]
    ordering = ["-created_at"]

    search_fields = ["name"]

    filterset_fields = {
        "id": ["gt", "gte", "lt", "lte"],
        "created_at": ["gt", "gte", "lt", "lte"],
        "updated_at": ["gt", "gte", "lt", "lte"],
        "name": ["exact", "contains"],
    }

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.select_related("owner")
    serializer_class = TaskSerializer

    ordering_fields = ["id", "created_at", "updated_at"]
    ordering = ["-created_at"]

    search_fields = ["title", "description"]

    filterset_fields = {
        "id": ["gt", "gte", "lt", "lte"],
        "created_at": ["gt", "gte", "lt", "lte"],
        "updated_at": ["gt", "gte", "lt", "lte"],
        "title": ["exact", "contains"],
        "description": ["exact", "contains"],
        "priority": ["exact"],
        "is_completed": ["exact"],
        "due_date": ["gt", "gte", "lt", "lte"],
        "project": ["exact"],
        "project__name": ["exact", "contains"],
        "tags": ["exact"],
        "tags__name": ["exact", "contains"],
    }

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(Q(owner=self.request.user) | Q(project__is_public=True))
        )
