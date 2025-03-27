from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    rental_contract = serializers.CharField()
    date = serializers.DateField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()
    payment_method = serializers.CharField()
