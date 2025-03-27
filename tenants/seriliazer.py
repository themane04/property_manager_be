from rest_framework import serializers


class TenantSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthday = serializers.DateField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(allow_blank=True, required=False)
    street = serializers.CharField(allow_blank=True, required=False)
    house_number = serializers.CharField(allow_blank=True, required=False)
    postal_code = serializers.CharField(allow_blank=True, required=False)
    city = serializers.CharField(allow_blank=True, required=False)
