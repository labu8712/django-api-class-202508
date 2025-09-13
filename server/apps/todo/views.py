from rest_framework.viewsets import ModelViewSet

from server.apps.todo.models import Project, Tag, Task
from server.apps.todo.serializers import (
    ProjectSerializer,
    TagSerializer,
    TaskSerializer,
)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
