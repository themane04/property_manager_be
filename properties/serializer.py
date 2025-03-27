from rest_framework import serializers


class PropertySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    street = serializers.CharField()
    house_number = serializers.CharField()
    postal_code = serializers.CharField()
    city = serializers.CharField()
    year_of_construction = serializers.IntegerField()
    flats_amount = serializers.IntegerField()
    park_spaces_amount = serializers.IntegerField()
    owner = serializers.CharField()
