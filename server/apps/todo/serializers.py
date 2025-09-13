from rest_framework.serializers import (
    # CurrentUserDefault,
    # HiddenField,
    ModelSerializer,
)

from server.apps.todo.models import Project, Tag, Task


class ProjectSerializer(ModelSerializer):
    # owner = HiddenField(default=CurrentUserDefault())

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
        read_only_fields = ["owner"]


class TagSerializer(ModelSerializer):
    # owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner"]


class TaskSerializer(ModelSerializer):
    # owner = HiddenField(default=CurrentUserDefault())

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
        read_only_fields = ["owner"]
