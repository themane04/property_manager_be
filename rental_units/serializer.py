from rest_framework import serializers

from features.serlializer import FeatureSerializer
from properties.serializer import PropertySerializer
from tenants.seriliazer import TenantSerializer


class RentalUnitSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    designation = serializers.CharField()
    type = serializers.CharField()
    area_m2 = serializers.IntegerField()
    number_of_rooms = serializers.IntegerField()
    rent = serializers.DecimalField(max_digits=10, decimal_places=2)
    available_from = serializers.DateField()
    status = serializers.CharField()
    tenant = TenantSerializer(read_only=True)
    properties = PropertySerializer(read_only=True)
    features = FeatureSerializer(many=True, read_only=True)
