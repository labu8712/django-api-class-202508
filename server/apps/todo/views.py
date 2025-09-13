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

    permission_classes = [IsAuthenticated, IsOwner]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.select_related("owner")
    serializer_class = TagSerializer

    ordering_fields = ["id", "created_at", "updated_at"]
    ordering = ["-created_at"]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.select_related("owner")
    serializer_class = TaskSerializer

    ordering_fields = ["id", "created_at", "updated_at"]
    ordering = ["-created_at"]
