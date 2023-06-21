from typing import Type

from rest_framework import serializers

from .models import Entry, PlayerDemography
from .validators import validate_user_tag


class ReportEntrySerializer(serializers.ModelSerializer):
    screenshot = serializers.ImageField(required=False, write_only=True)
    player_id = serializers.ReadOnlyField(source="player_id.username")

    class Meta:
        model = Entry
        read_only_fields = ["id", "player_id", "date_created"]
        exclude = ["toxicity", "emotion", "sentiment"]


class ReportSerializer(serializers.ModelSerializer):
    player_entries = ReportEntrySerializer(many=True, read_only=True)

    class Meta:
        model = PlayerDemography
        fields = "__all__"
        read_only_fields = ["id"]
        validators = [validate_user_tag]

    def validate(self, attrs):
        return super().validate(attrs)


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        read_only_fields = ["id", "date_created"]
        exclude = ["toxicity", "emotion", "sentiment"]
