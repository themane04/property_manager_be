from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from properties.models import Property
from properties.serializer import PropertySerializer


class PropertyListCreateView(APIView):
    def get(self, request):
        properties = Property.objects.all()
        if not properties:
            return Response({"message": "No properties found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            prop = Property(**serializer.validated_data)
            prop.save()
            return Response(PropertySerializer(prop).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Property.objects.get(id=pk)
        except Property.DoesNotExist:
            return None

    def get(self, request, pk):
        prop = self.get_object(pk)
        if prop is None:
            return Response({"message": "Property not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropertySerializer(prop)
        return Response(serializer.data)

    def patch(self, request, pk):
        prop = self.get_object(pk)
        if prop is None:
            return Response({"message": "Property not found."}, status=status.HTTP_404_NOT_FOUND)

        for attr, value in request.data.items():
            if attr != 'id':
                setattr(prop, attr, value)
        prop.save()
        return Response(PropertySerializer(prop).data)

    def delete(self, request, pk):
        prop = self.get_object(pk)
        if prop is None:
            return Response({"message": "Property not found."}, status=status.HTTP_404_NOT_FOUND)
        prop.delete()
        return Response({"message": "Property deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
