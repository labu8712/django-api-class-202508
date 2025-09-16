from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    PrimaryKeyRelatedField,
)

from server.apps.todo.models import Project, Tag, Task

User = get_user_model()


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProjectSerializer(ModelSerializer):
    owner_id = HiddenField(
        default=CurrentUserDefault(),
        source="owner",
        write_only=True,
    )
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "owner",
            "owner_id",
            "is_public",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner"]


class TagSerializer(ModelSerializer):
    owner_id = HiddenField(
        default=CurrentUserDefault(),
        source="owner",
        write_only=True,
    )
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "owner",
            "owner_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner"]


class TaskSerializer(ModelSerializer):
    owner_id = HiddenField(
        default=CurrentUserDefault(),
        source="owner",
        write_only=True,
    )
    owner = OwnerSerializer(read_only=True)

    project_id = PrimaryKeyRelatedField(
        source="project",
        queryset=Project.objects.all(),
        write_only=True,
    )
    project = ProjectSerializer(read_only=True)

    tag_ids = PrimaryKeyRelatedField(
        source="tags",
        queryset=Tag.objects.all(),
        write_only=True,
        many=True,
    )
    tags = TagSerializer(read_only=True, many=True)

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
            "owner_id",
            "project",
            "project_id",
            "tags",
            "tag_ids",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner"]
