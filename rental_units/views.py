from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from features.models import Feature
from properties.models import Property
from rental_units.models import RentalUnit
from rental_units.serializer import RentalUnitSerializer
from tenants.models import Tenant


class RentalUnitListCreateView(APIView):
    def get(self, request):
        units = RentalUnit.objects.all()
        if not units:
            return Response({"error": "No Rental units found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RentalUnitSerializer(units, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RentalUnitSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            property_id = request.data.get("property")
            tenant_id = request.data.get("tenant")
            features_ids = request.data.get("features", [])

            try:
                liegenschaft = Property.objects.get(id=property_id)
            except Property.DoesNotExist:
                return Response({"error": "Property not found."}, status=status.HTTP_404_NOT_FOUND)

            mieter = None
            if tenant_id:
                try:
                    mieter = Tenant.objects.get(id=tenant_id)
                except Tenant.DoesNotExist:
                    return Response({"error": "Tenant not found."}, status=status.HTTP_404_NOT_FOUND)

            features = list(Feature.objects.filter(id__in=features_ids))

            unit = RentalUnit(**data)
            unit.properties = liegenschaft
            unit.tenant = mieter
            unit.features = features
            unit.save()

            return Response(RentalUnitSerializer(unit).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalUnitDetailView(APIView):
    def patch(self, request, pk):
        try:
            unit = RentalUnit.objects.get(id=pk)
        except RentalUnit.DoesNotExist:
            return Response({"error": "Rental unit not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        if "features" in data:
            features_data = data["features"]
            feature_ids = [
                f["id"] if isinstance(f, dict) else f
                for f in features_data
            ]
            unit.features = Feature.objects.filter(id__in=feature_ids)
            del data["features"]

        if "properties" in data:
            property_val = data["properties"]
            property_id = property_val.get("id") if isinstance(property_val, dict) else property_val
            try:
                unit.properties = Property.objects.get(id=property_id)
            except Property.DoesNotExist:
                return Response({"error": "Property not found."}, status=status.HTTP_404_NOT_FOUND)
            del data["properties"]

        if "tenant" in data:
            tenant_val = data["tenant"]
            if isinstance(tenant_val, dict):
                tenant_id = tenant_val.get("id")
            else:
                tenant_id = tenant_val

            try:
                unit.tenant = Tenant.objects.get(id=tenant_id)
            except Tenant.DoesNotExist:
                return Response({"error": "Tenant not found."}, status=status.HTTP_404_NOT_FOUND)

            del data["tenant"]

        for attr, value in data.items():
            setattr(unit, attr, value)

        unit.save()
        return Response(RentalUnitSerializer(unit).data)

    def delete(self, request, pk):
        try:
            unit = RentalUnit.objects.get(id=pk)
        except RentalUnit.DoesNotExist:
            return Response({"error": "Rental unit not found."}, status=status.HTTP_404_NOT_FOUND)

        unit.delete()
        return Response({"message": "Rental unit deleted."}, status=status.HTTP_204_NO_CONTENT)
