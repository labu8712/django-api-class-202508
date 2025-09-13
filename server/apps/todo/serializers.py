from rest_framework.serializers import ModelSerializer

from server.apps.todo.models import Project, Tag, Task


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "owner",
            "is_public",
            "created_at",
            "updated_at",
        ]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "owner",
            "created_at",
            "updated_at",
        ]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "is_completed",
            "due_date",
            "owner",
            "project",
            "tags",
            "created_at",
            "updated_at",
        ]
