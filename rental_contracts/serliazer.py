from rest_framework import serializers

from rental_units.serializer import RentalUnitSerializer
from tenants.seriliazer import TenantSerializer


class RentalContractSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    tenant_id = serializers.CharField(write_only=True)
    rental_unit_id = serializers.CharField(write_only=True)
    tenant = TenantSerializer(read_only=True)
    rental_unit = RentalUnitSerializer(read_only=True)
    start_of_contract = serializers.DateField()
    end_of_contract = serializers.DateField()
    rent = serializers.DecimalField(max_digits=10, decimal_places=2)
    deposit = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()
