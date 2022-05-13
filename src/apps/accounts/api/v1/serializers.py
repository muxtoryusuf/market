from rest_framework import serializers
from apps.accounts.models import TradePoint, Visit


class TradePointSerializer(serializers.ModelSerializer):
    """Serializes Trade point."""

    class Meta:
        model = TradePoint
        fields = ("id", "title")


class VisitCreateSerializer(serializers.ModelSerializer):
    """Serializes creates a visit."""

    class Meta:
        model = Visit
        fields = (
            "market",
            "latitude",
            "longitude",
        )


class VisitSerializer(serializers.ModelSerializer):
    """Serializes visit."""

    class Meta:
        model = Visit
        fields = (
            "id",
            "created_at",
        )



