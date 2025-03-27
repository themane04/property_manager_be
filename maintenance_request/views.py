from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from maintenance_request.models import MaintenanceRequest
from maintenance_request.serializer import MaintenanceRequestSerializer
from rental_units.models import RentalUnit


class MaintenanceRequestListCreateView(APIView):
    def get(self, request):
        requests = MaintenanceRequest.objects.all()
        serializer = MaintenanceRequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaintenanceRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data["rental_unit"] = RentalUnit.objects.get(id=data["rental_unit"])
            request_obj = MaintenanceRequest(**data)
            request_obj.save()
            return Response(MaintenanceRequestSerializer(request_obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaintenanceRequestDetailView(APIView):
    def get_object(self, pk):
        try:
            return MaintenanceRequest.objects.get(id=pk)
        except MaintenanceRequest.DoesNotExist:
            return None

    def get(self, request, pk):
        request_obj = self.get_object(pk)
        if request_obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MaintenanceRequestSerializer(request_obj)
        return Response(serializer.data)

    def patch(self, request, pk):
        request_obj = self.get_object(pk)
        if request_obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        for attr, value in request.data.items():
            setattr(request_obj, attr, value)
        request_obj.save()
        return Response(MaintenanceRequestSerializer(request_obj).data)

    def delete(self, request, pk):
        request_obj = self.get_object(pk)
        if request_obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
