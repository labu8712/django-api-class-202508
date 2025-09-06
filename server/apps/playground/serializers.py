from rest_framework import serializers

from server.apps.playground.models import Item, ItemComment


class ItemCommentInItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemComment
        fields = ("id", "content", "created_at", "updated_at")


class ItemWithCommentSerializer(serializers.ModelSerializer):
    comments = ItemCommentInItemSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "description",
            "is_active",
            "comments",
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "description",
            "is_active",
        )
