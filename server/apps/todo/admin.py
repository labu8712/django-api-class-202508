from django.contrib import admin

from .models import Project, Tag, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "owner",
        "is_public",
        "created_at",
        "updated_at",
    )
    list_filter = ("owner", "is_public", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at", "updated_at")
    list_filter = ("owner", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "priority",
        "is_completed",
        "due_date",
        "owner",
        "project",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "is_completed",
        "due_date",
        "owner",
        "project",
        "created_at",
        "updated_at",
    )
    raw_id_fields = ("tags",)
    date_hierarchy = "created_at"
