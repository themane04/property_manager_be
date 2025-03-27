from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from tenants.models import Tenant
from tenants.seriliazer import TenantSerializer


class TenantListCreateView(APIView):
    def get(self, request):
        tenants = Tenant.objects.all()
        if not tenants:
            return Response({"message": "No tenants found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            tenant = Tenant(**serializer.validated_data)
            tenant.save()
            return Response(TenantSerializer(tenant).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TenantDetailView(APIView):
    def get_object(self, pk):
        try:
            return Tenant.objects.get(id=pk)
        except Tenant.DoesNotExist:
            return None

    def get(self, request, pk):
        tenant = self.get_object(pk)
        if tenant is None:
            return Response({"message": "Tenant not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data)

    def patch(self, request, pk):
        tenant = self.get_object(pk)
        if tenant is None:
            return Response({"message": "Tenant not found."}, status=status.HTTP_404_NOT_FOUND)

        for attr, value in request.data.items():
            if attr != 'id':
                setattr(tenant, attr, value)
        tenant.save()
        return Response(TenantSerializer(tenant).data)

    def delete(self, request, pk):
        tenant = self.get_object(pk)
        if tenant is None:
            return Response({"message": "Tenant not found."}, status=status.HTTP_404_NOT_FOUND)
        tenant.delete()
        return Response({"message": "Tenant deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
