from rest_framework import serializers

from main.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["label", "source", "time"]
