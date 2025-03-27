from rest_framework import serializers


class MaintenanceRequestSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    rental_unit = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
    created_at = serializers.DateField()
    assigned_craftsman = serializers.CharField()
