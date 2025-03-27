from rest_framework import serializers


class RentalContractSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    tenant = serializers.CharField()
    rental_unit = serializers.CharField()
    start_of_contract = serializers.DateField()
    end_of_contract = serializers.DateField()
    rent = serializers.DecimalField(max_digits=10, decimal_places=2)
    deposit = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()
