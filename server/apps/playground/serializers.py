from rest_framework import serializers

from server.apps.playground.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "description",
            "is_active",
        )
